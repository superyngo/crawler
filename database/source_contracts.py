lst_source_contracts = ['M04HA129', 'M04IA135', 'M04KA157', 'MAD04A2650', 'MAA04A2892', 'MA304A3081', 'M04LA118', 'MAC04A3401', 'MA704A3531', 'MA705A0221', 'MAC05A0271', 'MAC05A0431', 'MA705A0651', 'MA305A0911', 'MAC05A0861', 'MAC05A1091', 'MA705A1751', 'MAC05A1431', 'MA205A1571', 'MAC05A1731', 'MAC05A1741', 'MAC05A1781', 'MAC05A1941', 'MA305A2011', 'MA305A2012', 'MA805A2231', 'MA705A2471', 'MAC05A2631', 'MAC05A2671', 'MA805A2881', 'MAC05A3011', 'MA805A3481', 'MAC05A3471', 'MA705A3631', 'MAC05A3621', 'MA305A3611', 'MAC05A3781', 'MA705A3911', 'MAC05A4091', 'MA305A4181', 'MA805A4311', 'MA805A4211', 'MA705A4351', 'MAC05A4371', 'MAC05A4372', 'MA805A4431', 'MAB05A4391', 'MA705A4501', 'MAC05A4601', 'MA705A5331', 'MA705A4701', 'MAC05A4741', 'MA805A4821', 'MA805A4831', 'MA705A4961', 'MAC05A4981', 'MAC05A4982', 'MAC05A5151', 'MAC05A5191', 'MA805A5231', 'MA805A5241', 'MA805A5451', 'MA805A5631', 'MA705A4681', 'MA305A5741', 'MA705A5871', 'MA305A5951', 'MA705A6451', 'MA805A6521', 'MA805A6531', 'MA305A6501', 'MA305A6502', 'MA705A6711', 'MA805A6561', 'MA805A6641', 'MA805A6651', 'MA705A6811', 'MAS05A6861', 'MA805A6941', 'MA805A6991', 'MA805A6981', 'MA805A7061', 'MA805A7141', 'MA805A7071', 'MA805A7101', 'MA805A7191', 'MA705A7181', 'MAC06A0011', 'MA806A0211', 'MA806A0281', 'MA706A0271', 'MA806A0291', 'MA806A0401', 'M06BA080', 'MA806A0691', 'MA806A0821', 'MA806A0931', 'MA306A0971', 'MAS06A0991', 'MA806A1101', 'MA706A1111', 'MA706A1151', 'MA706A1181', 'MAS06A1231', 'MA706A1531', 'MA806A1641', 'MA806A1731', 'MA806A1741', 'MA806A1811', 'MA806A1951', 'MA806A2191', 'MA806A2271', 'MA706A2231', 'MA706A2421', 'MA806A2411', 'MAS06A2451', 'MA706A2461', 'MA806A2491', 'MA806A2521', 'MA706A2601', 'MA206A2651', 'MA806A2771', 'MA806A2841', 'MA706A3131', 'MAS06A2991', 'MAS06A3001', 'MA706A3031', 'MA706A3011', 'MAS06A3061', 'MAS06A3141', 'MA806A3251', 'MA706A3511', 'MAS06A3791', 'MA806A3821', 'MA806A3891', 'MA706A3961', 'MA806A4031', 'MA806A4211', 'MAS06A4371', 'MA306A4201', 'MA306A4202', 'MAS06A4421', 'MA806A4481', 'MA806A4541', 'MA806A4601', 'MAY06A4651', 'MAR06A4621', 'MAR06A4622', 'MA806A4681', 'MA806A4961', 'MA506A5053', 'MA206A5042', 'MA807A0191', 'MA707A0181', 'MA807A0361', 'MAR07A0311', 'MAR07A0312', 'MAR07A0313', 'MA807A0531', 'MA707A0591', 'MAS07A0671', 'MAR07A0911', 'MAS07A1021', 'MAS07A1091', 'MA707A1161', 'MA707A1331', 'MA707A1441', 'MA707A1621', 'MA707A1651', 'MA307A1081', 'MA307A1082', 'NA407A245M1', 'NA407A245M3', 'NA407A245M5', 'NA407A245M7', 'MA307A1661', 'MA707A1791', 'MA707A2081', 'MAS07A2061', 'MA707A2181', 'MA707A2381', 'MA307A2631', 'MA707A2731', 'MAB07A2841', 'MAB07A3001', 'MA707A3101', 'MA207A3332', 'MA708A0061', 'MA708A0071', 'MA708A0091', 'MAE08A0122', 'MA708A0201', 'MA708A0411', 'MAY08A0631', 'MA208A0652', 'MAS08A0731', 'MA908A0821', 'MA708A0871', 'MA908A0921', 'MA708A1031', 'MA208A1091', 'MA208A1092', 'MA908A1631', 'MA708A1661', 'MAS08A1691', 'MAE08A1892', 'MA908A1931', 'MA708A2031', 'MA208A2041', 'MAS08A2171', 'MAE08A2211', 'MAE08A2212', 'MA208A2221', 'MAS08A2281', 'MA808A2601', 'MA208A2762', 'MA708A2791', 'MA908A3071', 'MAS08A3161', 'MA708A3201', 'MAB08A3492', 'NAL08A4783', 'MAE08A3601', 'MAE08A3602', 'MAE08A3762', 'MA208A3881', 'MA208A3882', 'MA308A3811', 'MA708A3851', 'MA708A3991', 'MA208A3972', 'MAE08A3982', 'MA508A3953', 'MA908A4011', 'MAS09A0051', 'MA708A4151', 'MA708A4152', 'NA408A551M1', 'MAY09A0441', 'DCD09A1301', 'MA209A0521', 'MAS09A0661', 'MAY09A0781', 'MA209A0791', 'MA209A0941', 'MA209A0942', 'MA209A0943', 'MAB09A1041', 'MAE09A0451', 'MAE09A0452', 'MA309A1151', 'MAY09A1341', 'MA209A1421', 'MA709A1441', 'MA209A1561', 'MAB09A1691', 'MA709A1861', 'MAY09A1471', 'MA209A1741', 'MAY09A2091', 'MA909A2121', 'MA209A2111', 'MA309A2261', 'MA309A2262', 'MA909A2571', 'MA709A2551', 'MAE09A2731', 'MAE09A2732', 'MA308A3962', 'MA308A3964', 'MA709A3191', 'MA709A3291', 'DCH09A939M1', 'DCH09A939M2', 'DCH09A939M3', 'DCH09A939M4', 'DC609A9514', 'MA309A3431', 'MA909A3471', 'MA209A3561', 'MAS09A3581', 'MA209A3941', 'MA209A4082', 'MA509A4063', 'MAE09A4101', 'MAE09A4102', 'MAR09A4113', 'MA309A4141', 'MA309A4142', 'MAB09A4191', 'MA909A4281', 'MAA09A4292', 'MA909A4361', 'MAA09A4391', 'MAC09A4381', 'MAC09A4531', 'MAC09A4532', 'MAA09A4601', 'MAS10A0051', 'MA710A0461', 'MA210A0131', 'MA210A0181', 'MA710A0221', 'MA310A0291', 'MA710A0471', 'MA910A0711', 'MA710A0761', 'MAC10A0801', 'MA210A0831', 'MAE10A0891', 'MAE10A0892', 'MAK10A0971', 'MAK10A0972', 'MA210A1021', 'MAE10A1132', 'MAE10A1133', 'MA710A1121', 'MAC10A1201', 'MAS10A1251', 'MA710A1271', 'MA910A1391', 'DCH10A392M1', 'DCH10A392M2', 'MAE10A1461', 'MA910A1471', 'MA210A1583', 'MAR10A1631', 'MAE10A1621', 'MAE10A1622', 'MA210A1691', 'MAC10A1741', 'MAC10A1742', 'MA310A1771', 'MA710A1821', 'MAK10A1801', 'MAE10A1861', 'MAE10A1862', 'MA710A1721', 'MAS10A2061', 'MA310A2161', 'MA910A2301', 'MAK10A2461', 'MAA10A2522', 'MAA10A2523', 'MAE10A2544', 'MAS10A2641', 'MA710A2681', 'MAK10A2701', 'MA710A2781', 'MAA10A2811', 'MA910A2831', 'MA710A2821', 'MAK10A2891', 'MA310A2871', 'MAK10A2951', 'MA710A3001', 'MA710A3221', 'MA210A3072', 'MAR10A3141', 'MAS10A3281', 'MA710A3481', 'MA310A3351', 'MA710A3631', 'MA210A3581', 'MA210A3582', 'MA310A3611', 'MAK10A3641', 'MA310A3661', 'MA210A3721', 'MAK10A3741', 'MAE10A3831', 'MAA10A3881', 'MA310A3901', 'MAC10A3941', 'MAC10A3942', 'MAK10A3981', 'MAK10A4031', 'MAK10A4032', 'MAE10A4091', 'MAJ10A4123', 'MA210A4141', 'MAE10A4161', 'MAE10A4162', 'MAC10A4241', 'MA710A4301', 'MA510A4261', 'MA510A4262', 'MA510A4263', 'MA310A4311', 'MA310A4312', 'MAS10A4321', 'DC610B19531', 'DC610B19532', 'DC610B19533', 'MAK10A4351', 'MA710A4431', 'MAC10A4471', 'MAE10A4511', 'MAE10A4512', 'MA210A4631', 'MA710A4701', 'MA910A4711', 'MAJ10A4762', 'MAC10A4961', 'NA510A4684', 'MA710A5131', 'MA710A5132', '23K11A0031', 'MAS10A5171', '23Q11A0091', '23W11A0161', '23R11A0211', '23P11A0291', '23C11A0341', '23K11A0631', '23K11A0632', '23P11A0851', '23E11A0931', '23E11A0932', '23P11A0941', '23K11A0461', '23K11A0462', '23K11A1074', '23P11A1111', '23P11A1151', '23P11A0971', '23P11A0972', '23P11A0973', '23P11A0974', '23P11A0975']














