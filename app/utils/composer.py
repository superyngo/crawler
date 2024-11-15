from app.utils.common import fn_log
from app.utils.multithreading import multithreading
from types import MethodType
from typing import Optional, Any, Callable, Protocol
from abc import ABC

type Components = dict[str, Any]
type LoadableComponents = dict[str, Components]

class CsLoaderComponent:
    def __init__(self, *args, loadable_components: LoadableComponents):
        self._loadable_components: LoadableComponents = loadable_components
        self._loaded_components = set()
        if args: self.load_components(*args)
    def load_components(self, *args) -> None:
        if 'ALL' in args:
            args = set(self._loadable_components) - {'__loader__'}
        for task in args:
            if task in self._loaded_components:
                fn_log(f"{task} has already been loaded so skip")
                continue
            if task in set(self._loadable_components) - {'__loader__'}:
                for key, value in self._loadable_components[task].items():
                    match key:
                        case '__init__component':
                            MethodType(value, self)()
                        case '__remove__component':
                            pass
                        case _:
                            setattr(self, key, MethodType(value, self) if callable(value) else value)
            else:
                raise AttributeError(f"'{task}' is not a valid task for {self.__class__.__name__}, try {list(self._loadable_components.keys())} or 'ALL' ")
            if self._loadable_components.get('__loader__'): MethodType(self._loadable_components['__loader__']['__init__loader'], self)(task)
            self._loaded_components.add(task)
            fn_log(f"{task} loaded successfully")
        return None
    def remove_components(self, *args) -> None:
        if 'ALL' in args:
            args = set(self._loadable_components) - {'__loader__'}
        for task in args:
            if task in self._loaded_components:
                for key,value in self._loadable_components[task].items():
                    match key:
                        case '__init__component':
                            pass
                        case '__remove__component':
                            MethodType(value, self)()
                        case _:
                            if hasattr(self, key): delattr(self, key)
                if self._loadable_components.get('__loader__'): MethodType(self._loadable_components['__loader__']['__remove__loader'], self)(task)
                self._loaded_components.remove(task)
                fn_log(f"{task} removed successfully")
            else:
                raise AttributeError(f"'{task}' components is not loaded or component {task} doesn't exists")
        return None

class CsMultiSeed:
    def __init__(self, index):
        self._index = index


class Subclass_Ptl(Protocol):
    _index: int
    _close_instance: Callable
    _loadable_components: dict
class CsMultiManager_Ptl(Protocol):
    _instances:dict[int, Subclass_Ptl]
    _subclass:Callable
    _sources:dict
    _args:set[Any]
    _kwargs:dict[str, Any]

class CsMultiManager(CsMultiManager_Ptl):
    def __init__(self, *args, threads: int, subclass: CsMultiManager_Ptl, **kwargs) -> None: 
        for key, value in {'instances':{}, 'sources':{}, 'threads': 0, 'subclass': subclass, 'args': set(args), 'kwargs': kwargs}.items():
            setattr(self, '_' + key, value)
        # init instances
        self.threads = threads
    def _init_instances(self) -> None:
        def _init_instance(*args, index:int, **kwargs):
            if index in self._instances:
                fn_log(f"{index} instance already exists so pass")
                return
            fn_log(f"start initializing {index} instance")
            self._instances.update({index: self._subclass(*args, index=index, **kwargs)})
        multithreading(
            call_def = _init_instance,
            source = None,
            threads = self._threads,
            args = tuple(self._args),
            kwargs = self._kwargs
        )
    def _call_instances(self, handler:str, threads:Optional[int]=None) -> Callable:
        if threads is None: threads = self._threads 
        if threads <= 0: raise ValueError('threads must be positive integer( >0 )')
        def _def_wrapper(*args, source:Any=None, threads:int=threads, **kwargs):
            match threads:
                case _ if threads <= 0: raise ValueError('threads must be positive integer( >0 )')
                case _ if threads > self._threads: self.threads = threads
                case _: pass
            # split source into self._sources
            if isinstance(source,(list, tuple, dict)):
                self._sources.clear()
                multithreading(
                    call_def = lambda source, index: self._sources.update({index: source}),
                    source = source,
                    threads = threads,
                )
            # execute instances def
            multithreading(
                call_def = lambda *args, index, **kwargs: getattr(self._instances[index], handler)(*args, **kwargs),
                source = source,
                threads = threads,
                args = args,
                kwargs = kwargs
            )
        return _def_wrapper
    @property # Getter
    def threads(self) -> int:
        return self._threads
    @threads.setter # Setter
    def threads(self, threads: int) -> None:
        if not isinstance(threads, int) or threads < 0: raise TypeError(f"threads must > 0")
        match threads:
            case self._threads:
                fn_log(f"current threads {threads} unchanged")
            case _ if threads > self._threads:
                self._threads = threads
                self._init_instances()
            case _ if threads < self._threads:
                for i in range(threads, self._threads):
                    self._instances[i]._close_instance() 
                    self._instances.pop(i)
                self._threads = threads

class CsMultiLoaderEntry(CsMultiManager):
    def __init__(self):
        if self.threads == 0: self.threads = 1
        self._instances_loadable_components = self._instances[0]._loadable_components
        for task in self._args:
            for handler in self._instances_loadable_components[task]:
                if not task.startswith("_"):
                    setattr(self, handler, self._call_instances(handler=handler))
    def load_instances_components(self, *args, threads:Optional[int]=None) -> None:
        if 'ALL' in args:
            args = set(self._instances_loadable_components)
        for task in args:
            if task in self._args:
                fn_log(f"{task} has already been loaded so skip")
                continue
            if task in self._instances_loadable_components:
                # load component to instances
                self._call_instances(handler='load_components')(task)
                # set handler entrance for multi_manager
                for handler in self._instances_loadable_components[task]:
                    if not task.startswith("_"):
                        setattr(self, handler, self._call_instances(handler=handler, threads=threads))
            else:
                raise AttributeError(f"'{task}' is not a valid task for {self.__class__.__name__}, try {set(self._instances_loadable_components)} or 'ALL' ")
            self._args.add(task)
            fn_log(f"{task} entry loaded successfully")
    def remove_instances_components(self, *args) -> None:
        if 'ALL' in args: args = set(self._args)
        for task in args:
            if task in self._args:
                # remove component for instances
                self._call_instances('remove_components')(task)
                for key in self._instances_loadable_components[task]:
                    if 'handler' in key and hasattr(self, key):
                        delattr(self, key)
                self._args.remove(task)
                fn_log(f"{task} entry removed successfully")
            else:
                raise AttributeError(f"'{task}' components is not loaded or component {task} doesn't exists")
    def crawling_main(self, task, source:Optional[list]=None, threads:Optional[int]=None, **kwargs):
        if source:fn_log(f"Start {task}, total source count: {len(source)}, total threads: {threads}")
        
        # load task
        if task not in self._args: self.load_instances_components(task, threads=threads)
        
        # execute
        getattr(self, task + '_handler')(source = source, **kwargs)

class my_loader():
    def load_components(self, obj:object, **kwargs) -> None:
        for key, value in kwargs.items():
            match key:
                case '__init__component':
                    MethodType(value, obj)()
                case '__remove__component':
                    pass
                case _:
                        setattr(obj, key, MethodType(value, self) if callable(value) else value)
            fn_log(f"{key} loaded successfully")
    def remove_components(self, obj:object, **kwargs) -> None:
        for key,value in kwargs.items():
            match key:
                case '__init__component':
                    pass
                case '__remove__component':
                    MethodType(value, self)()
                case _:
                    if hasattr(obj, key): delattr(obj, key)
            fn_log(f"{key} removed successfully")

            
