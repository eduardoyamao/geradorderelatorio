
from docxtpl import DocxTemplate, InlineImage

# for height and width you have to use millimeters (Mm), inches or points(Pt) class :
from docx.shared import Mm
import jinja2

tpl = DocxTemplate('my_world_template.docx')

context = {
    'myimage': InlineImage(tpl, 'templates/foto.png', width=Mm(20)),
    'myimageratio': InlineImage(
        tpl, 'foto.jpg', width=Mm(30), height=Mm(60)
    ),
    'frameworks': [
        {
            'image': InlineImage(tpl, 'templates/foto.png', height=Mm(10)),
            'desc': 'legenda teste da foto.',
        },
    ],
}
tpl.render(context, jinja_env)
tpl.save('output/inline_image.docx')