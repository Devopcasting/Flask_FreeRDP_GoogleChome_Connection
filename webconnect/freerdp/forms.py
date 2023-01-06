from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,BooleanField,SelectField
from wtforms.validators import DataRequired,ValidationError
from webconnect.models import ConnectionDB

# FreeRDP Connection form
class FreeRDPForm(FlaskForm):
    connection_name = StringField('Connection Name',validators=[DataRequired()])
    server_address = StringField('Server Address',validators=[DataRequired()])
    user_name = StringField('Username')
    user_password = PasswordField('Username')
    domain_name = StringField('Domain')
    restric_admin_mode = BooleanField('Restricted admin mode')
    resolution_fullscreen = BooleanField('FullScreen',render_kw={'checked': True})
    resolution_multimon = BooleanField('Multimon')
    resolution_span = BooleanField('Span')
    sec_nla = BooleanField('NLA')
    sec_rdp = BooleanField('RDP')
    sec_tls = BooleanField('TLS')
    float_bar = BooleanField('Floatbar',render_kw={'checked': True})
    network_connection_type = SelectField('Network connection type',choices=[('none','None'),('auto','Auto-detect'),
    ('modem','Modem'),('broadband-low','Low performance broadband'),('broadband-high','High performance broadband'),('wan','WAN'),('lan','LAN')])
    submit = SubmitField('Create')

    # Check for duplicate connection name
    def validate_connection_name(self,connection_name):
        # Get FreeRDP Connection names
        freerdp_conn_names = ConnectionDB.query.filter_by(protocol="FreeRDP").all()
        for i in freerdp_conn_names:
            if i.connection_name == connection_name.data:
                raise ValidationError(f"Connection {connection_name.data} is already available.")

# Update FreeRDP Connection form
class UpdateFreeRDPForm(FlaskForm):
    connection_name = StringField('Connection Name',validators=[DataRequired()])
    server_address = StringField('Server Address',validators=[DataRequired()])
    user_name = StringField('Username')
    user_password = PasswordField('Username')
    domain_name = StringField('Domain')
    restric_admin_mode = BooleanField('Restricted admin mode')
    resolution_fullscreen = BooleanField('FullScreen')
    resolution_multimon = BooleanField('Multimon')
    resolution_span = BooleanField('Span')
    sec_nla = BooleanField('NLA')
    sec_rdp = BooleanField('RDP')
    sec_tls = BooleanField('TLS')
    float_bar = BooleanField('Floatbar')
    network_connection_type = SelectField('Network connection type',choices=[('none','None'),('auto','Auto-detect'),
    ('modem','Modem'),('broadband-low','Low performance broadband'),('broadband-high','High performance broadband'),('wan','WAN'),('lan','LAN')])
    submit = SubmitField('Update')