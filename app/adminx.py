#coding:utf-8
import xadmin
from xadmin import views
from models import OaActivitys,OaAdmin,OaFiles,OaFetchcompany,OaFetchpeople,OaFilesDiscuss,OaResAgentinfo,OaResBasicinfo,OaResCompany,OaResProject,OaResTrader
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from django.contrib.auth.models import User,Group,Permission

'''
class BaseSetting(object):
    enable_themes = True
    #不明
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSetting(object):
    global_search_models = [Boy, ]
    global_models_icon = {
        Boy: 'fa fa-laptop',
    }
    menu_style = 'accordion'#'accordion'
    site_title=u'站点标题'
    site_footer=u'公司明好吃呢个'
    def get_site_menu(self):
        return (
            {'title': '内容管理', 'perm': self.get_model_perm( Boy, 'change'), 'menus':(
                {'title': '游戏资料', 'icon': 'info-sign', 'url': self.get_model_url(Boy, 'changelist')},
                {'title': '组', 'icon': 'info-sign', 'url': self.get_model_url(Group, 'changelist')},
                {'title': '全县', 'icon': 'info-sign', 'url': self.get_model_url(Permission, 'changelist')},
                {'title': '用户', 'icon': 'info-sign', 'url': self.get_model_url(User, 'changelist')},
                {'title': '网站文章', 'icon': 'file', 'url': self.get_model_url(Boy, 'changelist') + '?_rel_categories__id__exact=1'},
            )},
            {'title': '分类管理', 'perm': self.get_model_perm(Boy, 'change'), 'menus':(
                {'title': '主要分类', 'url': self.get_model_url(Boy, 'changelist') + '?_p_parent__isnull=True'},
                {'title': '游戏资料', 'url': self.get_model_url(Boy, 'changelist') + '?_rel_parent__id__exact=2'},
            )},

        )
xadmin.site.register(views.CommAdminView, GlobalSetting)


class BoyAdmin(object):
    def open_web(self, instance):
        return "<a href='http://%s' target='_blank'>Open</a>" % instance.name
    open_web.short_description = "Acts"
    open_web.allow_tags = True
    open_web.is_column = True
    app_label=u'傻逼'
    #列表页展示内容
    list_display=('name','age','like','home','birthday','is_new','open_web','y')
    #列表页链接字段
    list_display_links = ('age',)
    #列表页顶部过滤器
    list_filter=('age','birthday','is_new',('like',xadmin.filters.MultiSelectFieldListFilter))
    #列表页顶部搜索
    search_fields=('name','age')
    #不明
    list_quick_filter = ['like', {'field': 'name', 'limit': 10}]
    #列表页细节展示
    show_detail_fields=('name',)
    #列表页编辑
    list_editable=('birthday','is_new','y')
    #不明
    batch_fields=('contact','age')
    #不明
    relfield_style = 'fk-ajax'
    #删除还原
    reversion_enable = True
    #添加新条目时的分步操作
    wizard_form_list = [
        ('First\'s Form', ('name', )),
        ('Second Form', ('birthday',)),
        ('Thread Form', ('age',))
    ]
    #自动刷新设置
    refresh_times = (3, 5, 10)
    #不明
    actions = None
    #列表页底部统计
    aggregate_fields = {"age": "sum"}
    #列表页可选布局
    grid_layouts = ('table', 'thumbnails')
    #书签
    list_bookmarks = [{'title': "Need Guarantee", 'query': {'age__exact': 16}, 'order': ('-age',),
                       'cols': ('name', 'birthday',)}]
    #修改页的布局
    # form_layout = (
    #     Col("col2",
    #         Fieldset('Record data',
    #                  'name', 'age',
    #                  css_class='unsort short_label no_title'
    #                  ),
    #         span=9, horizontal=True
    #         ),
    #     Col("col1",
    #         Fieldset('Comm data',
    #                  'is_new', 'home'
    #                  ),
    #         Fieldset('Maintain details',
    #                  'like', 'birthday'
    #                  ),
    #         span=3
    #         )
    # )
    form_layout = (
        Main(
            TabHolder(
                Tab('Comm Fields',
                    Fieldset('Company data',
                             'name', 'age',
                             description="some comm fields, required"
                             ),
                    # Inline(MaintainLog),
                    ),
                Tab('Extend Fields',
                    Fieldset('Contact details',
                             'name',
                             Row('name', 'like'),
                             Row('name', 'birthday'),
                             Row(AppendedText(
                                 'like', 'G'), AppendedText('name', "G")),
                             'birthday'
                             ),
                    ),
            ),
        ),
        Side(
            Fieldset('Status data',
                     'age', 'like', 'birthday'
                     ),
        )
    )
    #图表绘制
    data_charts = {
        u"aa1": {'title': u"统计表", "x-field": "age", "y-field": ("y","birthday"),"order":('age',)},
        u"aa2": {'title': u"统表", "x-field": "age", "y-field": "birthday", "order": ('age',)},
        "per_month": {'title': u"Monthly Users", "x-field": "_chart_month", "y-field": ("y",),"order":("age",),
                      "option": {
                          "series": {"bars": {"align": "center", "barWidth": 0.1, 'show': True}},
                          "xaxis": {"aggregate": "sum", "mode": "categories"},
                      },
                      },
    }
    def _chart_month(self,obj):
        return obj.birthday.strftime("%m")


xadmin.site.register(Boy,BoyAdmin)
'''
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSetting(object):
    global_search_models = [OaActivitys, OaFiles]
    global_models_icon = {
        OaActivitys: 'fa fa-cloud',
    }
    menu_style = 'accordion'#'accordion'
    site_title=u'招商局后台管理'
    site_footer=u'颐生科技有限公司'
    def get_site_menu(self):
        return (
            {'title': '资源管理','icon': 'fa fa-camera','perm': self.get_model_perm( OaResBasicinfo, 'view'), 'menus':(
                {'title': '基本信息库', 'icon': 'fa fa-list', 'url': self.get_model_url(OaResBasicinfo, 'changelist')},
                {'title': '客商资源库', 'icon': 'fa fa-book', 'url': self.get_model_url(OaResTrader, 'changelist')},
                {'title': '项目信息库', 'icon': 'fa fa-info-circle', 'url': self.get_model_url(OaResProject, 'changelist')},
                {'title': '媒介资源库', 'icon': 'fa fa-crosshairs', 'url': self.get_model_url(OaResAgentinfo, 'changelist')},
                {'title': '企业需求库', 'icon': 'fa fa-expand', 'url': self.get_model_url(OaResCompany, 'changelist')},
            )},
            {'title': '内容管理', 'icon': 'fa fa-camera', 'perm': self.get_model_perm(OaActivitys, 'view'), 'menus': (
                {'title': '游戏资料', 'icon': 'fa fa-cloud', 'url': self.get_model_url(OaActivitys, 'changelist')},
                {'title': '游戏资料', 'icon': 'fa fa-cloud', 'url': self.get_model_url(OaFiles, 'changelist')},
                {'title': '游戏资料', 'icon': 'fa fa-camera', 'url': self.get_model_url(OaActivitys, 'changelist')},
            )},

        )
xadmin.site.register(views.CommAdminView, GlobalSetting)

class OaActivitysAdmin(object):
    list_display=('id','name','time','address','content','company',)
    search_fields=('name',)

class OaFilesAdmin(object):
    list_display=('id',)

from django.forms import DateTimeField
class PermissionModelMultipleChoiceField(DateTimeField):

    def label_from_instance(self, p):
        print p
        print '[['
        return '111'


from xadmin import widgets
from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from xadmin.util import vendor
from xadmin.widgets import AdminTextareaWidget,AdminSplitDateTime,AdminDateWidget,AdminTimeWidget
from django.utils import timezone
from time import strftime

class MyDatatimeWidget(forms.DateInput):

    @property
    def media(self):
        return vendor('datepicker.js', 'datepicker.css', 'xadmin.widget.datetime.js','timepicker.js', 'timepicker.css')

    def __init__(self, attrs=None, format=None):
        final_attrs = {'class': 'date-field', 'size': '10'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(MyDatatimeWidget, self).__init__(attrs=final_attrs, format=format)

    def render(self, name, value, attrs=None):
        print value
        currTime=time.localtime(value)
        dateStr = time.strftime('%Y-%m-%d', currTime)
        timeStr = time.strftime('%H:%M:%S', currTime)
        print dateStr
        print timeStr
        # input_html1 = super(MyDatatimeWidget, self).render(name, value, attrs)
        input_html1 = super(MyDatatimeWidget, self).render(name, dateStr, attrs)
        input_html2 = super(MyDatatimeWidget, self).render(name, timeStr, attrs)
        print '~~~~~~~~~~~~~~~~'
        print input_html1
        return mark_safe('<div class="input-group date bootstrap-datepicker"><span class="input-group-addon"><i class="fa fa-calendar"></i></span>%s'
                         '<span class="input-group-btn"><button class="btn btn-default" type="button">%s</button></span></div>' % (input_html1, _(u'Today'))
                         +'<div class="input-group time bootstrap-timepicker"><span class="input-group-addon"><i class="fa fa-clock-o">'
                         '</i></span>%s<span class="input-group-btn"><button class="btn btn-default" type="button">%s</button></span></div>' % (input_html2, _(u'Now')))
class MyWidget(MyDatatimeWidget):


    def decompress(self, value):
        print 'decompress'
        print value
        bb=super(MyWidget, self).decompress(value)
        print bb
        return bb

    def format_output(self, rendered_widgets):
        print 'format_output'
        print rendered_widgets
        return super(MyWidget, self).format_output(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        print 'data----dict'
        print data
        print files
        print name
        # print data['start_time_0']+' '+data['start_time_1']
        # data['start_time']=int(time.mktime(time.strptime(data['start_time_0']+' '+data['start_time_1'], '%Y-%m-%d %H:%M:%S')))
        sdata={}
        sdata['start_time'] = 1111111111
        # for k in data:
        #     if k=='start_time':
        tempdata=' '.join(data.getlist(name))
        print tempdata
        sdata['start_time']=int(time.mktime(time.strptime(tempdata,'%Y-%m-%d %H:%M:%S')))
        print sdata['start_time']
        return super(MyWidget, self).value_from_datadict(sdata, files, name)


    def render(self, name, value, attrs=None):#form传进数据时
        print 'render'
        print name
        print value
        print attrs
        print '-----------'
        # # if value:
        # xxx=time.localtime(value)
        # print xxx
        # value=time.strftime('%Y-%m-%d %H:%M:%S',xxx)
        # value.tzinfo=timezone.now().tzinfo
        # print timezone.now().tzinfo
        # print '-------'
        # value='2016-08-01'
        cc=super(MyWidget, self).render(name, value, attrs)
        return cc




from xadmin.views.base import  filter_hook
import time
class OaResBasicinfoAdmin(object):
    list_display=('id','name','locstr','area','curr_state','plan_content','coop_way','company_name','linkman','linktel','start_time','status')
    # fields = list_display
    list_editable=('area','coop_way','start_time')
    save_as=True
    reversion_enable=True
    search_fields=('name',)
    list_filter=('name','coop_way')
    show_detail_fields=('name','locstr')
    app_label=u'gg'
    # style_fields = {"start_time": 'm2m_transfer'}
    def get_field_attrs(self, db_field, **kwargs):
        attrs = super(OaResBasicinfoAdmin, self).get_field_attrs(db_field, **kwargs)

        if db_field.name == 'start_time':
            attrs['widget'] = MyWidget
        return attrs

    def results(self):
        print 'res'
        results = []
        for obj in self.result_list:
            if obj.start_time:
                x=time.localtime(obj.start_time)
                print x
                obj.start_time=strftime('%Y-%m-%d %H:%M:%S',x)
            results.append(self.result_row(obj))
        return results


class OaResTraderAdmin(object):
    list_display=('id','name','tel','from_company','to_company','project_name','project_status','start_time','job','mailbox','status')
    list_editable=('project_status','tel','status')
    save_as=True
    reversion_enable=True
    search_fields=('name','project_name')
    list_filter=('project_status',)
    show_detail_fields=('name','to_company')

class OaResProjectAdmin(object):
    list_display=('id','name','content','investors_name','inverst_money','inverst_address','industry_name','company_name','start_time','end_time','setbacks','linkman','linktel','status')
    list_editable=('inverst_money','setbacks')
    save_as=True
    reversion_enable=True
    search_fields=('name',)
    list_filter=('setbacks',)
    show_detail_fields=('name','inverst_address')

class OaResAgentinfoAdmin(object):
    list_display=('id','company_name','company_intro','address','linkman','job','linktel','start_time','status')
    list_editable=('company_name',)
    save_as=True
    reversion_enable=True
    search_fields=('company_name',)
    list_filter=('status',)
    show_detail_fields=('company_intro',)

class OaResCompanyAdmin(object):
    list_display=('id','name','intro','address','linkman','linktel','need_people','need_tech','need_money','need_place','out_need_place','start_time','status')
    list_editable=('name','need_people','need_tech','need_money','need_place','out_need_place')
    save_as=True
    reversion_enable=True
    search_fields=('name',)
    list_filter=('status',)
    show_detail_fields=('name','linkman')

xadmin.site.register(OaActivitys,OaActivitysAdmin)
xadmin.site.register(OaFiles,OaFilesAdmin)
xadmin.site.register(OaResBasicinfo,OaResBasicinfoAdmin)
xadmin.site.register(OaResTrader,OaResTraderAdmin)
xadmin.site.register(OaResProject,OaResProjectAdmin)
xadmin.site.register(OaResAgentinfo,OaResAgentinfoAdmin)
xadmin.site.register(OaResCompany,OaResCompanyAdmin)
