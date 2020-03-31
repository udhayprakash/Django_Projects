// Global Variables
changed_row_data = {};

// Functions
function showTable(evt, dataToView) {
  var i, tab_content, tab_links;
  tab_content = document.getElementsByClassName("tab_content");
  for (i = 0; i < tab_content.length; i++) {
    tab_content[i].style.display = "none";
  }
  tab_links = document.getElementsByClassName("tab_links");
  for (i = 0; i < tab_links.length; i++) {
    tab_links[i].className = tab_links[i].className.replace(" active", "");
  }
  document.getElementById(dataToView).style.display = "block";
  evt.currentTarget.className += " active";
}

function getDatePicker() {
    // function to act as a class
    function Datepicker() {}

    // gets called once before the renderer is used
    Datepicker.prototype.init = function(params) {
        // create the cell
        this.eInput = document.createElement('input');
        this.eInput.value = params.value;

        // https://jqueryui.com/datepicker/
        $(this.eInput).datepicker({
            dateFormat: 'dd/mm/yy'
        });
    };

    // gets called once when grid ready to insert the element
    Datepicker.prototype.getGui = function() {
        return this.eInput;
    };

    // focus and select can be done after the gui is attached
    Datepicker.prototype.afterGuiAttached = function() {
        this.eInput.focus();
        this.eInput.select();
    };

    // returns the new value after editing
    Datepicker.prototype.getValue = function() {
        return this.eInput.value;
    };

    // any cleanup we need to be done here
    Datepicker.prototype.destroy = function() {
        // but this example is simple, no cleanup, we could
        // even leave this method out as it's optional
    };

    // if true, then this editor will appear in a popup
    Datepicker.prototype.isPopup = function() {
        // and we could leave this method out also, false is the default
        return false;
    };

    return Datepicker;
}

function getCookie(name) {
    // To get the value of a particular cookie
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (let i=0; i < cookies.length; i++){
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if(cookie.substring(0, name.length + 1) == (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function headerCellRendererSelectAll(params){
    var cb = document.createElement('input');
    cb.setAttribute('type', 'checkbox');
    cb.setAttribute('id', 'selectAllCheckbox');

    var eHeader = document.createElement('label');
    var eTitle = document.createTextNode(params.colDef.headerName);
    eHeader.appendChild(cb);
    eHeader.appendChild(eTitle);

    cb.addEventListener('change', function(e){
        if($(this)[0].checked) {
            _.forEach(vm.gridOptions.api.getModel().rowsAfterFilter, function(node){
                node.setSelected(true);
            })
        } else {
            _.forEach(vm.gridOptions.api.getModel().rowsAfterFilter, function(node){
                node.setSelected(false);
            })
        }
    });
    return eHeader;
}

function externalFilterChanged(tab_selected) {
    gridOptions.api.setFilterModel(null);
    let hardcodedFilter = gridOptions.api.getFilterModel();
    if (tab_selected == 'active') {
        hardcodedFilter = {action: {type: 'notContains', filter: 'archived'}}
    } else if (tab_selected == 'archive') {
        hardcodedFilter = {action: {type: 'contains', filter: 'archived'}}
    }
    gridOptions.api.setFilterModel(hardcodedFilter);
    gridOptions.api.onFilterChanged();
}

// aggrid related
var gridOptions = {
    // define grid columns
    columnDefs: [
        {
            headerName: '', field: 'select', checkboxSelection: true, width: 36,
            sortable: false, filter: false, suppressMenu: true, resizable: false,
            pinned: true, headerCheckboxSelection: true,
            headerCheckboxSelectionFilterOnly: headerCellRendererSelectAll
        },
        {headerName: 'id', field: 'id', hide: true},
        {headerName: 'Title', field: 'title', editable: true},
        {   headerName: 'Description', field: 'description', editable: true, width: 450
            // filter: 'agLargeTextCellEditor',
        },
        { headerName: "Target Date", field: "target_date", editable: true, cellEditor: "datePicker" },
        {
            headerName: 'Action', marryChildren: true, pinned: 'right',
            children: [
                {headerName: 'Last action', field: 'action', editable: true},
                {headerName: 'Submit', field: 'Submit', width: 100,
                   cellRenderer: function(params) {
                        return '<button type="button">Submit</button>';
                   }
                },
                {headerName: 'Created at', field: 'created_at', width: 200, columnGroupShow: 'open'  },
                {headerName: 'Last Updated at', field: 'updated_at', width: 150 },
            ]
        }
    ],
    floatingFilter: true,
    rowData: null,
    pagination: true,
    paginationAutoPageSize: true,
    animateRows: true,
    suppressRowClickSelection: true,
    rowSelection: 'multiple',
    enableCellChangeFlash: true,
    multiSortKey: 'ctrl',
    enableRangeSelection: true,
    defaultColDef: {
        sortable: true,
        resizable: true,
        filter: 'agTextColumnFilter',
        suppressMenu: true,
        width: 150
    },
    columnTypes: {
        numberColumn: {width: 83}
    },
    components:{
        datePicker: getDatePicker()
    },
};

// setup the grid after the page has finished loading
document.addEventListener('DOMContentLoaded', function() {
    // Get the modal
    var modal = document.getElementById("myModal");

    // Get the button that opens the modal
    var btn = document.getElementById("create_task_id");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal
    btn.onclick = function() {
      modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
      modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }


    var gridDiv = document.querySelector('#table_grid_id');
    new agGrid.Grid(gridDiv, gridOptions);
    console.clear();
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: window.origin + '/todo/tasks_api/',
        success: function(result) {
            console.log(result);
            gridOptions.api.setRowData(result);
//            gridOptions.onGridReady = function(params){
//                params.api.sizeColumnToFit();
//            }
            gridOptions.onCellValueChanged = function(params) {
                if (params.oldValue !== params.newValue){
                    // update Grid locally
                    params.api.updateRowData({update: [params.data]});

                    // Store in-memory for updating back in database
                    if (!changed_row_data[params.data.id]) {
                        changed_row_data[params.data.id] = {};
                    }
//                let clicked_column_name = params.column.colId;
//                    changed_row_data[params.data.id][clicked_column_name] = params.data; //params.newValue;
                    changed_row_data[params.data.id] = params.data; //params.newValue;
                    console.log('changed_row_data[params.data.id]', changed_row_data[params.data.id])
                }
            };
            gridOptions.onCellClicked = function(params) {
                let clicked_column_name = params.column.colId;
                if (clicked_column_name == 'Submit') {
                    $.ajax({
                        type: 'POST',
                        url: window.origin + '/todo/tasks_api/',
                        headers: {'X-CSRFToken': getCookie('csrftoken')},
                        data: JSON.stringify(changed_row_data[params.data.id]),
//                        data: JSON.stringify({'name': 'Udhay'}) ,
                        contentType: 'application/json;charset=utf-8',
                        dataType: 'json',
                        success: function(result) {
                        console.log(' In Success')
                        }
                    }).done(function(result) {
                        console.log('In Completed');
                    }).fail(function(e){
                        console.log('In FAIL:', e);
                    });
                }
            }
        }
    }).done(function(result) {
        console.log('Completed');
    }).fail(function(e){
        console.log('FAIL:', e);
    });


    $('#archive_task_id').click(function() {
        alert('clicked - archive task - button');

        let selected_rows = gridOptions.api.getSelectedRows();
        if(!selected_rows){
            alert('select atleast one row!');
            return false;
        }

        let selected_ids = selected_rows.map(function(each_row){
            return each_row.id;
        });

        $.ajax({
            type: 'POST',
            url: window.origin + '/todo/tasks_api/',
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            data: JSON.stringify({
                'action': 'archive',
                'selected_ids': selected_ids
            }),
            contentType: 'application/json;charset=utf-8',
            dataType: 'json',
            success: function(result) {
            console.log(' In Success')
            }
        }).done(function(result) {
            console.log('In Completed');
            alert('task archived');
        }).fail(function(e){
            console.log('In FAIL:', e);
        });
    });

    $('#delete_task_id').click(function() {
        alert('clicked - delete task - button');

        let selected_rows = gridOptions.api.getSelectedRows();
        if(!selected_rows){
            alert('select atleast one row!');
            return false;
        }

        let selected_ids = selected_rows.map(function(each_row){
            return each_row.id;
        });

        $.ajax({
            type: 'POST',
            url: window.origin + '/todo/tasks_api/',
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            data: JSON.stringify({
                'action': 'delete',
                'selected_ids': selected_ids
            }),
            contentType: 'application/json;charset=utf-8',
            dataType: 'json',
            success: function(result) {
            console.log(' In Success')
            }
        }).done(function(result) {
            console.log('In Completed');
            alert('task deleted');
        }).fail(function(e){
            console.log('In FAIL:', e);
        });
    });

    $('#create_task_form_id').click(function() {
        console.log('clicked - create task - button');

        let title = document.getElementById('title_id').value;
        let description = document.getElementById('description_id').value;
        let target_date = document.getElementById('target_date_id').value;

        if ( title && description && target_date) {
            $.ajax({
                type: 'CREATE',
                url: window.origin + '/todo/tasks_api/',
                headers: {'X-CSRFToken': getCookie('csrftoken')},
                data: JSON.stringify({
                    'title': title,
                    'description': description,
                    'target_date': target_date
                }),
                contentType: 'application/json;charset=utf-8',
                dataType: 'json',
                success: function(result) {
                console.log(' In Success')
                }
            }).done(function(result) {
                console.log('In Completed');
                alert('New Task created');
            }).fail(function(e){
                console.log('In FAIL:', e);
            });
        } else {
            alert('Invalid submission');
        }
    });
});