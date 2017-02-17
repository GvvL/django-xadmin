#coding:utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from time import strftime
import logging
logging.getLogger(__name__)



COOP_WAY = (
    (0, u"合租"),
    (1, u"出让"),
    (2, u"出租"),
    (3, u"夏天的"),
)
SETBACKS=(
    (0,u'未开工'),
    (1,u'已开工'),
    (2,u'暂停')
)
PROJECT_STATUS=(
    (0,u'未开工'),
    (1,u'已开工'),
    (2,u'暂停')
)


class OaActivitys(models.Model):
    id = models.AutoField(u'序号',primary_key=True)  # AutoField?
    name = models.CharField(u'活动名称',max_length=255, blank=True,null=True)
    time = models.IntegerField(u'活动时间',blank=True, null=True)
    address = models.CharField(u'活动地点',max_length=255, blank=True,null=True)
    content = models.CharField(u'内容',max_length=255, blank=True)
    company = models.CharField(u'组织单位',max_length=255, blank=True)
    start_time = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'oa_activitys'
        verbose_name=u'活动'
        verbose_name_plural=verbose_name


class OaAdmin(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    uname = models.CharField(max_length=50,blank=True,null=True)
    nickname = models.CharField(max_length=50, blank=True)
    pwd = models.CharField(max_length=50)
    tel = models.BigIntegerField(blank=True, null=True)
    pid = models.IntegerField()
    last_ip = models.CharField(max_length=20, blank=True)
    last_time = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=False)
    group_id = models.IntegerField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'oa_admin'


class OaFetchcompany(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=55, blank=True)
    props = models.CharField(max_length=54, blank=True)
    company = models.CharField(max_length=55, blank=True)
    fetch_time = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True)
    start_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oa_fetchcompany'


class OaFetchpeople(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=55, blank=True)
    from_company = models.CharField(max_length=55, blank=True)
    to_company = models.CharField(max_length=55, blank=True)
    profession = models.CharField(max_length=55, blank=True)
    fetch_time = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True)
    start_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oa_fetchpeople'


class OaFiles(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    number = models.CharField(max_length=55, blank=True)
    title = models.CharField(max_length=55)
    from_group_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    urgent_level = models.IntegerField(blank=True, null=True)
    secret_level = models.IntegerField(blank=True, null=True)
    handler_default = models.CharField(max_length=255, blank=True)
    handler_history = models.CharField(max_length=255, blank=True)
    dispatch_default = models.CharField(max_length=255, blank=True)
    dispatch_history = models.CharField(max_length=255, blank=True)
    extra_file = models.CharField(max_length=255, blank=True)
    file_type = models.IntegerField(default=1)
    note = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=True)
    is_end = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'oa_files'
        verbose_name=u'文件'
        verbose_name_plural=verbose_name


class OaFilesDiscuss(models.Model):
    files_id = models.IntegerField()
    admin_id = models.IntegerField()
    discuss = models.CharField(max_length=255, blank=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oa_files_discuss'

'''
class OaGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    lower = models.CharField(max_length=2000)
    pid = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oa_group'


class OaLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    admin_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=255, blank=True)
    time = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'oa_log'


class OaLower(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    active = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    level = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    iconfont = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'oa_lower'


class OaProjectStart(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=25, blank=True)
    buid_address = models.CharField(max_length=255, blank=True)
    investors_name = models.CharField(max_length=25, blank=True)
    investors_prop = models.CharField(max_length=255, blank=True)
    coop_way = models.IntegerField()
    buid_content = models.CharField(max_length=255, blank=True)
    invest_money = models.FloatField()
    had_invest_money = models.FloatField()
    industry_name = models.CharField(max_length=255, blank=True)
    linkman = models.CharField(max_length=25, blank=True)
    linktel = models.CharField(max_length=20, blank=True)
    is_transform = models.IntegerField()
    is_register = models.IntegerField()
    is_pass = models.IntegerField()
    start_time = models.IntegerField(blank=True, null=True)
    register_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oa_project_start'


class OaProjectTalk(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=40, blank=True)
    content = models.CharField(max_length=255, blank=True)
    investors_name = models.CharField(max_length=25, blank=True)
    investors_status = models.CharField(max_length=255, blank=True)
    industry_name = models.CharField(max_length=25, blank=True)
    inverst_money = models.FloatField()
    referrer = models.CharField(max_length=15, blank=True)
    talker = models.CharField(max_length=15, blank=True)
    start_time = models.IntegerField(blank=True, null=True)
    is_keypoint = models.IntegerField()
    progress = models.IntegerField()
    qaa = models.CharField(max_length=255, blank=True)
    linkman = models.CharField(max_length=25, blank=True)
    linktel = models.CharField(max_length=15, blank=True)
    is_pass = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oa_project_talk'


class OaPromissionapply(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    apply_id = models.IntegerField(blank=True, null=True)
    pass_id = models.IntegerField(blank=True, null=True)
    controller = models.CharField(max_length=55, blank=True)
    action = models.CharField(max_length=55, blank=True)
    apply_time = models.IntegerField(blank=True, null=True)
    pass_time = models.IntegerField(blank=True, null=True)
    is_pass = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oa_promissionapply'

'''
class OaResAgentinfo(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    company_name = models.CharField(u'单位名称',max_length=20, blank=True)
    company_intro = models.CharField(u'单位介绍',max_length=50, blank=True)
    address = models.CharField(u'单位地址',max_length=25, blank=True)
    linkman = models.CharField(u'联系人',max_length=10, blank=True)
    job = models.CharField(u'所处职位',max_length=30, blank=True)
    linktel = models.IntegerField(u'联系电话',blank=True, null=True)
    status = models.BooleanField(u'状态',default=True)
    start_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oa_res_agentinfo'
        verbose_name=u'媒介资源'
        verbose_name_plural=verbose_name

class UnixTimestampField(models.DateTimeField):
    """UnixTimestampField: creates a DateTimeField that is represented on the
    database as a TIMESTAMP field rather than the usual DATETIME field.
    """
    def __init__(self, null=False, blank=False, **kwargs):
        super(UnixTimestampField, self).__init__(**kwargs)
        # default for TIMESTAMP is NOT NULL unlike most fields, so we have to
        # cheat a little:
        logging.info("UnixTimestampField")
        self.blank, self.isnull = blank, null
        self.null = True # To prevent the framework from shoving in "not null".



    def to_python(self, value):
        print("to_python")
        logging.info(value)
        if isinstance(value, int):
            return datetime.fromtimestamp(value)
        else:
            return models.DateTimeField.to_python(self, value)

    def get_prep_value(self, value, connection, prepared=False):
        print("get_prep_value")
        if value==None:
            return None
        # Use '%Y%m%d%H%M%S' for MySQL < 4.1
        return strftime('%Y-%m-%d %H:%M:%S',value.timetuple())
    def get_db_prep_value(self, value, connection, prepared=False):
        # Casts datetimes into the format expected by the backend
        print("get_db_prep_value")
        return None
    def value_to_string(self, obj):
        print("value_to_string")
        val = self._get_val_from_obj(obj)
        return '' if val is None else val.isoformat()

    # def formfield(self, **kwargs):
    #     print("formfield")
    #     super(UnixTimestampField, self).formfield(**kwargs)
import time
class OaResBasicinfo(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(u'厂房名称',max_length=10, blank=True)
    locstr = models.CharField(u'地址',max_length=255, blank=True)
    area = models.IntegerField(u'面积',blank=True, null=True)
    curr_state = models.CharField(u'当前状态',max_length=20, blank=True)
    plan_content = models.CharField(u'计划内容',max_length=255, blank=True)
    coop_way = models.IntegerField(u'合作方式',choices=COOP_WAY,default=0)
    company_name = models.CharField(u'单位名称',max_length=20, blank=True)
    linkman = models.CharField(u'联系人',max_length=11)
    linktel = models.CharField(u'联系电话',max_length=11, blank=True)
    status = models.BooleanField(u'状态',default=True)
    start_time = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'oa_res_basicinfo'
        verbose_name=u'基本信息'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name


class OaResCompany(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(u'单位名称',max_length=25, blank=True)
    intro = models.CharField(u'单位介绍',max_length=255, blank=True)
    address = models.CharField(u'单位地址',max_length=25, blank=True)
    linkman = models.CharField(u'单位联系人',max_length=25, blank=True)
    linktel = models.CharField(u'联系电话',max_length=20, blank=True)
    need_people = models.CharField(u'人才需求',max_length=55, blank=True)
    need_tech = models.CharField(u'技术需求',max_length=55, blank=True)
    need_money = models.CharField(u'资金需求',max_length=55, blank=True)
    need_place = models.CharField(u'场地需求',max_length=255, blank=True)
    out_need_place = models.CharField(u'闲置场地需求',max_length=255, blank=True)
    status = models.BooleanField(u'状态',default=True)
    start_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oa_res_company'
        verbose_name=u'企业需求'
        verbose_name_plural=verbose_name


class OaResProject(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(u'项目名称',max_length=255)
    content = models.CharField(u'项目内容',max_length=255, blank=True)
    investors_name = models.CharField(u'投资方',max_length=11, blank=True)
    inverst_money = models.IntegerField(u'投资金额(万元)',blank=True, null=True)
    inverst_address = models.CharField(u'投资方地址',max_length=45, blank=True)
    industry_name = models.CharField(u'所处行业',max_length=11, blank=True)
    company_name = models.CharField(u'洽谈单位',max_length=21)
    start_time = models.IntegerField(u'开工时间',blank=True, null=True)
    end_time = models.IntegerField(u'结束时间',blank=True, null=True)
    setbacks = models.IntegerField(u'当前进度',choices=SETBACKS,default=0)
    qaa = models.CharField(u'问题及建议',max_length=255, blank=True)
    linkman = models.CharField(u'项目联系人',max_length=25)
    linktel = models.CharField(u'联系电话',max_length=20, blank=True)
    status = models.BooleanField(u'状态',default=True)

    class Meta:
        managed = False
        db_table = 'oa_res_project'
        verbose_name=u'项目资源'
        verbose_name_plural=verbose_name


class OaResTrader(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(u'客商姓名',max_length=10, blank=True)
    tel = models.CharField(u'电话',max_length=20, blank=True)
    from_company = models.CharField(u'所在单位',max_length=20)
    to_company = models.CharField(u'洽谈单位',max_length=255, blank=True)
    project_name = models.CharField(u'洽谈项目名称',max_length=255, blank=True)
    project_status = models.IntegerField(u'项目状态',choices=PROJECT_STATUS,default=0)
    start_time = models.IntegerField(u'开工时间',blank=True, null=True)
    job = models.CharField(u'所处职位',max_length=25, blank=True)
    mailbox = models.EmailField(u'邮箱',max_length=25, blank=True)
    status = models.BooleanField(u'状态',default=True)

    class Meta:
        managed = False
        db_table = 'oa_res_trader'
        verbose_name=u'客商资源'
        verbose_name_plural=verbose_name

'''
class OaWarning(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    msg = models.CharField(max_length=255, blank=True)
    time = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'oa_warning'


class OaWorkMsg(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    msg_no = models.IntegerField()
    msg_title = models.CharField(max_length=255, blank=True)
    msg_content = models.TextField(blank=True)
    msg_type = models.IntegerField()
    start_time = models.IntegerField()
    msg_from = models.IntegerField()
    msg_to = models.CharField(max_length=255, blank=True)
    msg_has_recive = models.CharField(max_length=255, blank=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oa_work_msg'


class ZsAdmin(models.Model):
    adminid = models.IntegerField(primary_key=True)
    adminname = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    groupid = models.IntegerField(blank=True, null=True)
    super = models.IntegerField(blank=True, null=True)
    timeline = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    logintimeline = models.IntegerField(blank=True, null=True)
    logintimes = models.IntegerField(blank=True, null=True)
    loginip = models.CharField(max_length=50, blank=True)
    memo = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'zs_admin'


class ZsArticle(models.Model):
    articleid = models.IntegerField(primary_key=True)
    catid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=50, blank=True)
    thumbfiles = models.CharField(max_length=255, blank=True)
    uploadfiles = models.CharField(max_length=255, blank=True)
    summary = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True)
    istop = models.IntegerField(blank=True, null=True)
    elite = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    adduser = models.CharField(max_length=50, blank=True)
    addtime = models.IntegerField(blank=True, null=True)
    updatetime = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    linktype = models.IntegerField(blank=True, null=True)
    linkurl = models.CharField(max_length=255, blank=True)
    purview = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True)
    metakeyword = models.CharField(max_length=255, blank=True)
    metadescription = models.CharField(max_length=500, blank=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zs_article'


class ZsCategory(models.Model):
    catid = models.IntegerField(primary_key=True)
    modalias = models.CharField(max_length=50, blank=True)
    catname = models.CharField(max_length=100, blank=True)
    pcatid = models.IntegerField(blank=True, null=True)
    ismenu = models.IntegerField(blank=True, null=True)
    showindex = models.IntegerField()
    icon = models.CharField(max_length=8, blank=True)
    depth = models.IntegerField()
    ord = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True)
    urltype = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zs_category'


class ZsLog(models.Model):
    logid = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=50, blank=True)
    ip = models.CharField(max_length=50, blank=True)
    content = models.CharField(max_length=255, blank=True)
    logtype = models.IntegerField(blank=True, null=True)
    timeline = models.IntegerField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zs_log'


class ZsPhoto(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    modalias = models.CharField(max_length=50, blank=True)
    catid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    thumbfiles = models.CharField(max_length=255, blank=True)
    uploadfiles = models.CharField(max_length=255, blank=True)
    albums = models.TextField(blank=True)
    summary = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True)
    istop = models.IntegerField(blank=True, null=True)
    elite = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    adduser = models.CharField(max_length=50, blank=True)
    addtime = models.IntegerField(blank=True, null=True)
    updatetime = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    linktype = models.IntegerField(blank=True, null=True)
    linkurl = models.CharField(max_length=255, blank=True)
    purview = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True)
    metakeyword = models.CharField(max_length=255, blank=True)
    metadescription = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'zs_photo'


class ZsPhotoAttr(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    modalias = models.CharField(max_length=50, blank=True)
    aid = models.IntegerField(blank=True, null=True)
    extvalue = models.TextField(blank=True)
    relid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zs_photo_attr'


class ZsProject(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=255, blank=True)
    typeid = models.IntegerField(blank=True, null=True)
    photoid = models.IntegerField(blank=True, null=True)
    addtime = models.IntegerField()
    updatetime = models.IntegerField(blank=True, null=True)
    progress = models.IntegerField()
    status = models.IntegerField()
    istop = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zs_project'


class ZsProjectAttr(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'zs_project_attr'


class ZsResource(models.Model):
    resid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    typeid = models.IntegerField(blank=True, null=True)
    photoid = models.IntegerField(blank=True, null=True)
    addtime = models.IntegerField()
    updatetime = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    istop = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zs_resource'


class ZsResourceAttr(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zs_resource_attr'
'''
