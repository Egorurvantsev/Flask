from flask import redirect, url_for
from flask_admin import expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class DefaultAdminView(ModelView):
    column_display_pk = True
    can_export = True
    export_types = ('csv', 'xlsx')

    def create_blueprint(self, admin):
        blueprint = super().create_blueprint(admin)
        blueprint.name = f'{blueprint.name}_admin'
        return blueprint

    def get_url(self, endpoint, **kwargs):
        if not (endpoint.startswith('.') or endpoint.startswith('admin.')):
            endpoint = endpoint.replace('.', '_admin.')
        return super().get_url(endpoint, **kwargs)

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))


class CustomAdminIndexView(DefaultAdminView):
    pass
    # @expose()
    # def index(self):
    #     if not (current_user.is_authenticated and current_user.is_staff):
    #         return redirect(url_for('auth.login'))
    #     return super().index()


class TagAdminView(CustomAdminIndexView):
    column_searchable_list = ['name']
    column_editable_list = ['name']


class ArticleAdminView(CustomAdminIndexView):
    column_searchable_list = ['title']
    column_filters = ['author_id']
    form_excluded_columns = ('created_at', 'updated_at')
    column_editable_list = ('title', 'text')


class UserAdminView(CustomAdminIndexView):
    column_exclude_list = ('password')
    form_excluded_columns = ('password')
    column_export_exclude_list = ('password')
    column_searchable_list = ['email']
    column_editable_list = ('firstname', 'lastname', 'is_staff')


class AuthorAdminView(CustomAdminIndexView):
    column_searchable_list = ['id', 'user_id']
    form_columns = ['id', 'user_id']
    column_list = ['id', 'user_id']

