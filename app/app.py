from dash import Dash

from config import Config
import top
from models import asset_manager


app = Dash(__name__)
app.title = Config.title
asset_manager.init(app.get_asset_url)

app.layout = top.create_view()

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
