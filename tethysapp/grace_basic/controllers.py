from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import *
import csv, os
from datetime import datetime
from tethys_sdk.workspaces import app_workspace

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )


    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }

    return render(request, 'grace_basic/home.html', context)

# @login_required
def home_graph(request, id):
    """
    Controller for home page to display a graph and map.
    """

    # Set up the graph options
    project_directory = os.path.dirname(__file__)
    app_workspace = os.path.join(project_directory, 'workspaces', 'app_workspace')
    csv_file = os.path.join(app_workspace, 'output' , id,  'hydrograph.csv')
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        csvlist = list(reader)
    volume_time_series = []
    formatter_string = "%m/%d/%Y"
    print(csvlist)
    for item in csvlist:
        mydate = datetime.strptime(item[0], formatter_string)
        volume_time_series.append([mydate, float(item[1])])

    # Configure the time series Plot View
    grace_plot = TimeSeries(
        engine='highcharts',
        title= id + ' GRACE Data',
        y_axis_title='Volume',
        y_axis_units='cm',
        y_min=None,
        series=[
            {
                'name': 'Change in Volume',
                'color': '#0066ff',
                'data': volume_time_series,
            },
        ],
        width='100%',
        height='300px'
    )

    context = {'grace_plot': grace_plot,
               'reg_id': id}

    return render(request, 'grace_basic/home.html', context)