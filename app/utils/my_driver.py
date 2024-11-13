# 20241014
from app.utils.multithreading import *
from app.utils.common import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, TimeoutException, NoAlertPresentException, JavascriptException
from types import MethodType
from typing import Self

class CsMyDriverComponent: 
    def _select_change_value(self:Self, By_locator: str, locator: str, new_value: str) -> None:
        _select_element = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By_locator, locator)))
        _select_element = Select(_select_element)  # Create a Select instance
        _select_element.select_by_value(new_value)
    def _input_send_keys(self, By_locator: str, locator: str, new_value: str) -> None:
        _input_element = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By_locator, locator)))
        _input_element.clear()
        _input_element.send_keys(new_value)
    def _wait_element(self, By_locator: str, locator: str, time: int = 1000, condition=EC.presence_of_element_located):
        try:
            return WebDriverWait(self, time).until(condition((By_locator, locator)))
        except UnexpectedAlertPresentException:
            try:
                self.switch_to.alert.accept()
            except NoAlertPresentException:
                pass
            return WebDriverWait(self, time).until(condition((By_locator, locator)))
    def _try_extract_element_value(self, element, error_return = "") -> str:
        try:
            match element.tag_name:
                case 'input' | 'textarea':
                    if element.get_attribute('type') == 'checkbox':
                        return element.get_attribute('checked')
                    return element.get_attribute('value')
                case 'select':
                    return Select(element).first_selected_option.text
                case _:
                    return element.text
        except NoSuchElementException:
            return error_return

class CsMyEdgeDriverInit:
    def __init__(self, user_data_dir):
        import logging
        Service = webdriver.EdgeService
        Options = webdriver.EdgeOptions
        # Suppress selenium and webdriver_manager logs
        logging.getLogger('selenium').setLevel(logging.WARNING)
        logging.getLogger('urllib3').setLevel(logging.WARNING)
        logging.getLogger('webdriver_manager').setLevel(logging.WARNING)
        # Set up paths
        user_data_dir = os.path.abspath(user_data_dir)
        log_path = os.path.abspath("./logs/edge_driver.log")

        # Create directories if they don't exist
        os.makedirs(user_data_dir, exist_ok=True)
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        edge_bin = './app/bin/msedgedriver.exe'
        service_args=[
                    #   '--log-level=ALL',
                    #   '--append-log',
                    #   '--readable-timestamp',
                    '--disable-build-check',
                    ]
        service = Service(executable_path=edge_bin, service_args=service_args)
        options = Options()
        options.unhandled_prompt_behavior = 'accept'
        options.add_argument('--inprivate')
        # options.add_argument(f"user-data-dir={user_data_dir}")
        options.add_argument("--disable-notifications")
        options.add_argument("--log-level=3")
        super(type(self),self).__init__(service=service, options=options)
        self.int_main_window_handle = self.current_window_handle

class CsLoaderComponent:
    def __init__(self, *args, loadable_components: dict):
        self._loadable_components = loadable_components
        self._loaded_components = set()
        if args: self.load_components(*args)
    def load_components(self, *args) -> None:
        if 'ALL' in args:
            args = set(self._loadable_components) - {'_loader_init_remove'}
        for task in args:
            if task in self._loaded_components:
                fn_log(f"{task} has already been loaded so skip")
                continue
            if task in set(self._loadable_components) - {'_loader_init_remove'}:
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
            if self._loadable_components.get('_loader_init_remove'): MethodType(self._loadable_components['_loader_init_remove']['__init__loader'], self)(task)
            self._loaded_components.add(task)
            fn_log(f"{task} loaded successfully")
        return None
    def remove_components(self, *args) -> None:
        if 'ALL' in args:
            args = set(self._loadable_components) - {'_loader_init_remove'}
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
                if self._loadable_components.get('_loader_init_remove'): MethodType(self._loadable_components['_loader_init_remove']['__remove__loader'], self)(task)
                self._loaded_components.remove(task)
                fn_log(f"{task} removed successfully")
            else:
                raise AttributeError(f"'{task}' components is not loaded or component {task} doesn't exists")
        return None

class CsMultiSeed:
    def __init__(self, index):
        self._index = index
    def _close_instance(self):
        if self._helper_driver:
            self._helper_driver.close()
        self.close() # depends on the instance
        self.quit()

class CsMultiManager:
    def __init__(self, *args, threads, subclass, **kwargs) -> None: 
        for key, value in {'instances':{}, 'sources':{}, 'threads': 0, 'subclass': subclass, 'args': set(args), 'kwargs': kwargs}.items():
            setattr(self, '_' + key, value)
        # init instances
        self.threads = threads
    def _init_instances(self) -> None:
        def _init_instance(*args, index, **kwargs):
            if index in self._instances:
                fn_log(f"{index} instance already exists so pass")
                return
            fn_log(f"start initializing {index} instance")
            self._instances.update({index: self._subclass(*args, index=index, **kwargs)})
        multithreading(
            call_def = _init_instance,
            source = None,
            threads = self._threads,
            args = self._args,
            kwargs = self._kwargs
        )
    def _call_instances(self, handler:str, threads:int=None) -> Callable:
        if threads is None: threads = self._threads 
        if threads <= 0: raise ValueError('threads must be positive integer( >0 )')
        def _def_wrapper(*args, source:any=None, threads:int=threads, **kwargs):
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

class CsMultiLoaderEntry:
    def __init__(self):
        if self.threads == 0: self.threads = 1
        self._instances_loadable_components = self._instances[0]._loadable_components
        for task in self._args:
            for handler in self._instances_loadable_components[task]:
                if not task.startswith("_"):
                    setattr(self, handler, self._call_instances(handler=handler))
    def load_instances_components(self, *args, threads:int=None) -> None:
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
    def crawling_main(self, task, source=None, threads=None, **kwargs):
        fn_log(f"Start {task}, total source count : {len(source)}")
        
        # load task
        if task not in self._args: self.load_instances_components(task, threads=threads)
        
        # execute
        getattr(self, task + '_handler')(source = source, **kwargs)

