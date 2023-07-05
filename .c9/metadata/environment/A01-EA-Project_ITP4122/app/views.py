{"filter":false,"title":"views.py","tooltip":"/A01-EA-Project_ITP4122/app/views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":93,"column":0},"action":"remove","lines":["from flask_appbuilder import ModelView","from flask_appbuilder.fieldwidgets import Select2Widget","from flask_appbuilder.models.sqla.interface import SQLAInterface","from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory","from wtforms.ext.sqlalchemy.fields import QuerySelectField","from app import appbuilder, db","from flask_appbuilder.baseviews import expose, BaseView","","","def department_query():","    return db.session.query(Department)","","","class EmployeeHistoryView(ModelView):","    datamodel = SQLAInterface(EmployeeHistory)","    #base_permissions = ['can_add', 'can_show']","    list_columns = ['department', 'begin_date', 'end_date']","","","class EmployeeView(ModelView):","    datamodel = SQLAInterface(Employee)","","    list_columns = ['full_name', 'department.name', 'employee_number']","    edit_form_extra_fields = {'department':  QuerySelectField('Department',","                                query_factory=department_query,","                                widget=Select2Widget(extra_classes=\"readonly\"))}","","","    related_views = [EmployeeHistoryView]","    show_template = 'appbuilder/general/model/show_cascade.html'","","","class FunctionView(ModelView):","    datamodel = SQLAInterface(Function)","    related_views = [EmployeeView]","","","class DepartmentView(ModelView):","    datamodel = SQLAInterface(Department)","    related_views = [EmployeeView]","","","class BenefitView(ModelView):","    datamodel = SQLAInterface(Benefit)","    add_columns = ['name']","    edit_columns = ['name']","    show_columns = ['name']","    list_columns = ['name']","","class MenuItemView(ModelView):","    datamodel = SQLAInterface(MenuItem)","    list_columns = ['id', 'name', 'link', 'menu_category_id']","","class MenuCategoryView(ModelView):","    datamodel = SQLAInterface(MenuCategory)","    list_columns = ['id', 'name']","","class NewsView(ModelView):","    datamodel = SQLAInterface(News)","    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']","","class NewsCategoryView(ModelView):","    datamodel = SQLAInterface(NewsCategory)","    list_columns = ['id', 'name']","","class NewsPageView(BaseView):","    default_view = 'local_news'","","    @expose('/local_news/')","    def local_news(self):","        param1 = 'Local News'","        self.update_redirect()","        return self.render_template('news.html', param1 = param1)","","    @expose('/global_news/')","    def global_news(self):","        param1 = 'Global News'","        self.update_redirect()","        return self.render_template('news.html', param1=param1)","","","db.create_all()","","\"\"\" Page View \"\"\"","appbuilder.add_view(NewsPageView, 'Local News', category=\"News\")","appbuilder.add_link(\"Global News\", href=\"/newspageview/global_news/\", category=\"News\")","","\"\"\" Custom Views \"\"\"","appbuilder.add_view(MenuItemView, \"MenuItem\", icon=\"fa-folder-open-o\", category=\"Admin\")","appbuilder.add_view(MenuCategoryView, \"MenuCategory\", icon=\"fa-folder-open-o\", category=\"Admin\")","appbuilder.add_view(NewsView, \"News\", icon=\"fa-folder-open-o\", category=\"Admin\")","appbuilder.add_view(NewsCategoryView, \"NewsCategory\", icon=\"fa-folder-open-o\", category=\"Admin\")","",""],"id":4},{"start":{"row":0,"column":0},"end":{"row":68,"column":1},"action":"insert","lines":["from flask_appbuilder import ModelView","from flask_appbuilder.fields import QuerySelectField","from flask_appbuilder.fieldwidgets import Select2Widget","from flask_appbuilder.models.sqla.interface import SQLAInterface","","from . import appbuilder, db","from .models import Benefit, Department, Employee, EmployeeHistory, Function","","","def department_query():","    return db.session.query(Department)","","","class EmployeeHistoryView(ModelView):","    datamodel = SQLAInterface(EmployeeHistory)","    # base_permissions = ['can_add', 'can_show']","    list_columns = [\"department\", \"begin_date\", \"end_date\"]","","","class EmployeeView(ModelView):","    datamodel = SQLAInterface(Employee)","","    list_columns = [\"full_name\", \"department.name\", \"employee_number\"]","    edit_form_extra_fields = {","        \"department\": QuerySelectField(","            \"Department\",","            query_func=department_query,","            widget=Select2Widget(extra_classes=\"readonly\"),","        )","    }","","    related_views = [EmployeeHistoryView]","    show_template = \"appbuilder/general/model/show_cascade.html\"","","","class FunctionView(ModelView):","    datamodel = SQLAInterface(Function)","    related_views = [EmployeeView]","","","class DepartmentView(ModelView):","    datamodel = SQLAInterface(Department)","    related_views = [EmployeeView]","","","class BenefitView(ModelView):","    datamodel = SQLAInterface(Benefit)","    add_columns = [\"name\"]","    edit_columns = [\"name\"]","    show_columns = [\"name\"]","    list_columns = [\"name\"]","","","db.create_all()","","appbuilder.add_view_no_menu(EmployeeHistoryView, \"EmployeeHistoryView\")","appbuilder.add_view(","    EmployeeView, \"Employees\", icon=\"fa-folder-open-o\", category=\"Company\"",")","appbuilder.add_separator(\"Company\")","appbuilder.add_view(","    DepartmentView, \"Departments\", icon=\"fa-folder-open-o\", category=\"Company\"",")","appbuilder.add_view(","    FunctionView, \"Functions\", icon=\"fa-folder-open-o\", category=\"Company\"",")","appbuilder.add_view(","    BenefitView, \"Benefits\", icon=\"fa-folder-open-o\", category=\"Company\"",")"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":19,"column":30},"end":{"row":19,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1688479787191,"hash":"2c5925509935f18ef058a7cb6cf13eae6f5381f7"}