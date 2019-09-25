import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['dash.css']
app =dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout =html.Div(children =[html.H1(children ='Hello Dash'), 
html.Div(children= '''Ehealth4everyone: Data Analytics BrainBox '''),
dcc.Graph(
    id= 'example-graph',
    figure={
        'data': [
            {'x': [1,2,3], 'y': [4,3,6], 'type': 'bar', 'name': 'SF'},
            {'x': [1,2,3], 'y': [7,2,3], 'type': 'bar', 'name' : 'Montreal'},
            {'x': [1,2,3], 'y': [1,4,5], 'type': 'bar', 'name' : 'Utaka'}


        ]
    , 'layout': {
        'title': 'Ehealth4everyone Data Visualization'
    }
    }

) 

])

if __name__ =='__main__':
    app.run_server(debug=True)
