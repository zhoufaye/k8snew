# Generated by Django 2.0.2 on 2018-08-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180804_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaiGou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cai_gou_ri_qi', models.CharField(max_length=200, verbose_name='采购日期')),
                ('chang_jia', models.CharField(max_length=200, verbose_name='厂家')),
                ('chang_ku_ming_cheng', models.CharField(max_length=200, verbose_name='仓库名称')),
                ('cai_gou_fang_shi', models.CharField(max_length=200, verbose_name='采购方式')),
                ('pin_pai', models.CharField(max_length=200, verbose_name='品牌')),
                ('xing_hao', models.CharField(blank=True, max_length=200, verbose_name='型号')),
                ('gui_ge', models.CharField(max_length=200, verbose_name='规格')),
                ('dan_jia', models.CharField(max_length=200, verbose_name='单价')),
                ('shu_liang', models.CharField(max_length=200, verbose_name='数量')),
                ('jin_e', models.CharField(max_length=200, verbose_name='金额')),
                ('che_chuan_hao', models.CharField(max_length=200, verbose_name='车船号')),
                ('yun_jia', models.CharField(max_length=200, verbose_name='运价')),
                ('yun_fei', models.CharField(max_length=200, verbose_name='运费')),
                ('cao_zuo_yuan', models.CharField(max_length=200, verbose_name='操作员')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
            ],
            options={
                'verbose_name': '采购登记',
                'verbose_name_plural': '采购登记',
            },
        ),
        migrations.CreateModel(
            name='CaiGouFuKuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ri_qi', models.CharField(max_length=200, verbose_name='日期')),
                ('cang_jia', models.CharField(max_length=200, verbose_name='厂家')),
                ('qian_kuan_jin_e', models.CharField(max_length=200, verbose_name='欠款金额')),
                ('fu_kuan_jin_e', models.CharField(max_length=200, verbose_name='付款金额')),
                ('cao_zuo_yuan', models.CharField(max_length=200, verbose_name='操作员')),
                ('da_yin', models.CharField(max_length=200, verbose_name='打印')),
            ],
            options={
                'verbose_name': '采购付款',
                'verbose_name_plural': '采购付款',
            },
        ),
        migrations.CreateModel(
            name='CaiGouSunHao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ri_qi', models.CharField(max_length=200, verbose_name='日期')),
                ('cang_ku_ming_cheng', models.CharField(max_length=200, verbose_name='仓库名称')),
                ('cang_jia', models.CharField(max_length=200, verbose_name='厂家')),
                ('pin_pai', models.CharField(max_length=200, verbose_name='品牌')),
                ('xing_hao', models.CharField(max_length=200, verbose_name='型号')),
                ('gui_ge', models.CharField(blank=True, max_length=200, verbose_name='规格')),
                ('sun_hao_shu_liang', models.CharField(max_length=200, verbose_name='损耗数量')),
                ('cao_zuo_yuan', models.CharField(max_length=200, verbose_name='操作员')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
            ],
            options={
                'verbose_name': '采购损耗',
                'verbose_name_plural': '采购损耗',
            },
        ),
        migrations.CreateModel(
            name='CaiGouYunFeiJieSuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ri_qi', models.CharField(max_length=200, verbose_name='日期')),
                ('che_chuan_hao', models.CharField(max_length=200, verbose_name='车船号')),
                ('dang_qian_yun_fei', models.CharField(max_length=200, verbose_name='当前运费')),
                ('jie_suan_yun_fei', models.CharField(max_length=200, verbose_name='结算运费')),
                ('cao_zuo_yuan', models.CharField(max_length=200, verbose_name='操作员')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
            ],
            options={
                'verbose_name': '采购运费结算',
                'verbose_name_plural': '采购运费结算',
            },
        ),
        migrations.CreateModel(
            name='CheLiang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhuang_xie_gong', models.CharField(max_length=200, verbose_name='车号')),
                ('si_ji', models.CharField(max_length=200, verbose_name='司机')),
                ('dian_hua1', models.CharField(max_length=200, verbose_name='联系电话1')),
                ('dian_hua2', models.CharField(max_length=200, verbose_name='联系电话2')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
            ],
            options={
                'verbose_name': '车辆信息',
                'verbose_name_plural': '车辆信息',
            },
        ),
        migrations.CreateModel(
            name='DangQianKuCun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chang_ku_ming_cheng', models.CharField(max_length=200, verbose_name='仓库名称')),
                ('cang_jia', models.CharField(max_length=200, verbose_name='厂家')),
                ('pin_pai', models.CharField(max_length=200, verbose_name='品牌')),
                ('xing_hao', models.CharField(max_length=200, verbose_name='型号')),
                ('gui_ge', models.CharField(max_length=200, verbose_name='规格')),
                ('cai_gou_shu_liang', models.CharField(max_length=200, verbose_name='采购数量')),
                ('song_huo_shu_liang', models.CharField(max_length=200, verbose_name='送货数量')),
                ('sun_hao_shu_liang', models.CharField(max_length=200, verbose_name='损耗数量')),
                ('ku_cun_shu_liang', models.CharField(max_length=200, verbose_name='库存数量')),
            ],
            options={
                'verbose_name': '订单库存',
                'verbose_name_plural': '订单库存',
            },
        ),
        migrations.CreateModel(
            name='DanWei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhuang_xie_gong', models.CharField(max_length=200, verbose_name='单位名称')),
                ('dianhua1', models.CharField(max_length=200, verbose_name='联系人')),
                ('dianhua2', models.CharField(max_length=200, verbose_name='联系电话')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
            ],
            options={
                'verbose_name': '单位信息',
                'verbose_name_plural': '单位信息',
            },
        ),
        migrations.CreateModel(
            name='ShuiNi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ri_qi', models.CharField(max_length=200, verbose_name='日期')),
                ('qu_yu', models.CharField(max_length=200, verbose_name='区域')),
                ('ke_hu_ming_cheng', models.CharField(max_length=200, verbose_name='客户名称')),
                ('wei_fu_huo_kuan', models.CharField(max_length=200, verbose_name='未付货款')),
                ('fu_kuan_jin_e', models.CharField(max_length=200, verbose_name='付款金额')),
                ('da_xie', models.CharField(max_length=200, verbose_name='大写')),
                ('fu_kuan_fang_shi', models.CharField(max_length=200, verbose_name='付款方式')),
                ('sheng_yu_huo_kuan', models.CharField(max_length=200, verbose_name='剩余货款')),
                ('cao_zuo_yuan', models.CharField(max_length=200, verbose_name='操作员')),
                ('da_yin', models.CharField(max_length=200, verbose_name='打印')),
            ],
            options={
                'verbose_name': '水泥货款',
                'verbose_name_plural': '水泥货款',
            },
        ),
        migrations.CreateModel(
            name='SiJiJieSuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ri_qi', models.CharField(max_length=200, verbose_name='日期')),
                ('che_pai_hao', models.CharField(max_length=200, verbose_name='车牌号')),
                ('si_ji_xing_ming', models.CharField(max_length=200, verbose_name='司机姓名')),
                ('si_ji_dian_hua', models.CharField(max_length=200, verbose_name='司机电话')),
                ('dang_qian_yun_fei', models.CharField(max_length=200, verbose_name='当前运费')),
                ('fu_yun_fei', models.CharField(blank=True, max_length=200, verbose_name='付运费')),
                ('fu_kuan_fang_shi', models.CharField(max_length=200, verbose_name='付款方式')),
                ('wei_fu_yun_fei', models.CharField(max_length=200, verbose_name='未付运费')),
                ('cao_zuo_yuan', models.CharField(max_length=200, verbose_name='操作员')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
                ('da_yin', models.CharField(max_length=200, verbose_name='打印')),
            ],
            options={
                'verbose_name': '司机结算',
                'verbose_name_plural': '司机结算',
            },
        ),
        migrations.CreateModel(
            name='XiaoShouDengJi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dan_hao', models.CharField(max_length=200, verbose_name='单号')),
                ('ri_qi', models.CharField(max_length=200, verbose_name='日期')),
                ('qu_yu', models.CharField(max_length=200, verbose_name='区域')),
                ('dian_hua2', models.CharField(max_length=200, verbose_name='客户名称')),
                ('ke_hu_bian_hao', models.CharField(blank=True, max_length=200, verbose_name='司机')),
                ('si_ji_dian_hua', models.CharField(max_length=200, verbose_name='司机电话')),
                ('fu_kuan_fang_shi', models.CharField(max_length=200, verbose_name='付款方式')),
                ('jin_e', models.CharField(max_length=200, verbose_name='金额')),
                ('you_hui_jin_e', models.CharField(max_length=200, verbose_name='优惠金额')),
                ('yin_shou_jin_e', models.CharField(max_length=200, verbose_name='应收金额')),
                ('shi_shou_jin_e', models.CharField(blank=True, max_length=200, verbose_name='实收金额')),
                ('cao_zuo_yuan', models.CharField(max_length=200, verbose_name='操作员')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
                ('da_yin', models.CharField(max_length=200, verbose_name='打印')),
            ],
            options={
                'verbose_name': '销售登记',
                'verbose_name_plural': '销售登记',
            },
        ),
        migrations.CreateModel(
            name='ZhuangXieJieSuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ri_qi', models.CharField(max_length=200, verbose_name='日期')),
                ('zhuang_xie_gong', models.CharField(max_length=200, verbose_name='装卸工')),
                ('dang_qian_zhuang_xie', models.CharField(max_length=200, verbose_name='当前装卸')),
                ('fu_zhuang_xie_fei', models.CharField(max_length=200, verbose_name='付装卸费')),
                ('wei_fu_zhuang_xie', models.CharField(max_length=200, verbose_name='未付装卸')),
                ('cao_zuo_yuan', models.CharField(max_length=200, verbose_name='操作员')),
                ('bei_zhu', models.CharField(max_length=200, verbose_name='备注')),
                ('da_yin', models.CharField(max_length=200, verbose_name='打印')),
            ],
            options={
                'verbose_name': '装卸结算',
                'verbose_name_plural': '装卸结算',
            },
        ),
        migrations.RenameModel(
            old_name='zhuang_xie_gong_xin_xi',
            new_name='ZhuangXieGongXinXi',
        ),
        migrations.AlterModelOptions(
            name='gongshangxinxi',
            options={'verbose_name': '供应商信息', 'verbose_name_plural': '供应商信息'},
        ),
        migrations.AlterModelOptions(
            name='kehuxinxi',
            options={'verbose_name': '客户信息', 'verbose_name_plural': '客户信息'},
        ),
        migrations.AlterModelOptions(
            name='shuinixinxi',
            options={'verbose_name': '水泥信息', 'verbose_name_plural': '水泥信息'},
        ),
        migrations.AlterModelOptions(
            name='zhuangxiegongxinxi',
            options={'verbose_name': '装卸工信息', 'verbose_name_plural': '装卸工信息'},
        ),
        migrations.AlterField(
            model_name='kehuxinxi',
            name='ke_hu_bian_hao',
            field=models.CharField(blank=True, max_length=200, verbose_name='客户编号'),
        ),
    ]
