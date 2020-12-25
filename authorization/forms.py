"""Formularios del módulo Permission."""

# Django
from django import forms

# Models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# Forms
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Fieldset, Layout, Div, Reset

# Utils
from authorization.models import ContentType, Permission

User = get_user_model()


class PermissionForm(forms.ModelForm):
    """Formulario de permisos."""

    def __init__(self, *args, **kwargs):
        """Inicializacion del Formulario."""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div(
                    Div('name', css_class='col-4'),
                    css_class='row'
                ),
                Div(
                    Div('content_type', css_class='col-4'),
                    css_class='row'
                ),
                Div(
                    Div('codename', css_class='col-4'),
                    css_class='row'
                ),
            ),
            FormActions(
                Submit('submit', 'Guardar', css_class='float-right'),
                Reset('reset', 'Limpiar', css_class='float-right')
            )
        )

    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(
            app_label__in=['accounting', 'auth', 'authorization', 'core'],
            model__in=[
                 'archivo',
                 'cliente', 'factura', 'ordencompra', 'cobranza',
                 'proveedor', 'facturaproveedor', 'pago',
                 'mediopago',
                 'permission', 'user', 'group'
            ]
        ).order_by('model'), label='Modulo'
    )

    class Meta:
        """Configuraciones de formulario."""

        model = Permission
        fields = ('name', 'content_type', 'codename')


class GroupForm(forms.ModelForm):
    """Formulario de group."""

    def __init__(self, *args, **kwargs):
        """Inicializacion del Formulario."""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['permissions'].widget.attrs['size'] = 10
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div(
                    Div('name', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    Div('permissions', css_class='col-6', size=20),
                    css_class='row'
                ),
            ),
            FormActions(
                Submit('submit', 'Guardar', css_class='float-right'),
                Reset('reset', 'Limpiar', css_class='float-right')
            )
        )

    permissions = forms.ModelMultipleChoiceField(
         queryset=Permission.objects.filter(
             content_type__app_label__in=['accounting', 'auth', 'authorization', 'core'],
             content_type__model__in=[
                 'archivo',
                 'cliente', 'factura', 'ordencompra', 'cobranza',
                 'proveedor', 'facturaproveedor', 'pago',
                 'mediopago',
                 'permission', 'user', 'group'
             ]
         ).order_by('content_type__model', 'name')
    )

    class Meta:
        """Configuraciones de formulario."""

        model = Group
        fields = ('name', 'permissions')


class UserForm(forms.ModelForm):
    """Formulario de usuario."""

    def __init__(self, *args, **kwargs):
        """Inicializacion del Formulario."""
        super().__init__(*args, **kwargs)
        # Remuevo campo password si es para editar
        if self.instance and self.instance.pk:
            self.fields.pop('password', None)
        self.helper = FormHelper()
        self.fields['groups'].widget.attrs['size'] = 10
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div(
                    Div('username', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    Div('first_name', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    Div('last_name', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    Div('password', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    Div('groups', css_class='col-6'),
                    css_class='row'
                ),
            ),
            FormActions(
                Submit('submit', 'Guardar', css_class='float-right'),
                Reset('reset', 'Limpiar', css_class='float-right')
            )
        )

    class Meta:
        """Configuraciones de formulario."""

        model = User
        fields = (
            'username', 'first_name', 'last_name', 'password',
            'groups'
        )
