// Global Variables
changed_row_data = {};

// Functions
function getCookie(name) {
    // To get the value of a particular cookie
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function headerCellRendererSelectAll(params) {
    var cb = document.createElement('input');
    cb.setAttribute('type', 'checkbox');
    cb.setAttribute('id', 'selectAllCheckbox');

    var eHeader = document.createElement('label');
    var eTitle = document.createTextNode(params.colDef.headerName);
    eHeader.appendChild(cb);
    eHeader.appendChild(eTitle);

    cb.addEventListener('change', function (e) {
        if ($(this)[0].checked) {
            _.forEach(vm.gridOptions.api.getModel().rowsAfterFilter, function (node) {
                node.setSelected(true);
            })
        } else {
            _.forEach(vm.gridOptions.api.getModel().rowsAfterFilter, function (node) {
                node.setSelected(false);
            })
        }
    });
    return eHeader;
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
        {headerName: 'Cluster Name', field: 'cluster_name', width: 150},
        {
            headerName: 'No. of Nodes', field: 'nodes_count', editable: is_staff === "True",
            filter: 'agNumberColumnFilter',
        },
        {
            headerName: 'Submit', field: 'Submit', width: 100,
            cellRenderer: function (params) {
                return '<button type="button">Update</button>';
            }, hide: is_staff !== "True"
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
    }
};

// setup the grid after the page has finished loading
document.addEventListener('DOMContentLoaded', function () {
    if (is_staff === "True") {
        // Get the modal
        var modal = document.getElementById("myModal");

        // Get the button that opens the modal
        var btn = document.getElementById("create_cluster_id");

        // Get the <span> element that closes the modal
        var span = document.getElementsByClassName("close")[0];

        // When the user clicks the button, open the modal
        btn.onclick = function () {
            modal.style.display = "block";
        };

        // When the user clicks on <span> (x), close the modal
        span.onclick = function () {
            modal.style.display = "none";
        };

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        };

    }
    let gridDiv = document.querySelector('#table_grid_id');
    new agGrid.Grid(gridDiv, gridOptions);
    console.clear();
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: window.origin + '/Clusters/',
        success: function (result) {
            gridOptions.api.setRowData(result);
            gridOptions.onGridReady = function (params) {
                params.api.sizeColumnToFit();
            };
            gridOptions.onCellValueChanged = function (params) {
                if (params.oldValue !== params.newValue) {
                    // update Grid locally
                    params.api.updateRowData({update: [params.data]});

                    // Store in-memory for updating back in database
                    if (!changed_row_data[params.data.id]) {
                        changed_row_data[params.data.id] = {};
                    }
                    changed_row_data[params.data.id] = params.data; //params.newValue;
                }
            };
            gridOptions.onCellClicked = function (params) {
                if (params.column.colId === 'Submit') {
                    $.ajax({
                        type: 'POST',
                        url: window.origin + '/clusters_api/',
                        headers: {'X-CSRFToken': getCookie('csrftoken')},
                        data: JSON.stringify(changed_row_data[params.data.id]),
                        contentType: 'application/json;charset=utf-8',
                        dataType: 'json',
                        success: function (result) {
                            console.log(' In Success')
                        }
                    }).done(function (result) {
                        console.log('In Completed');
                        location.forcedReload(true);
                    }).fail(function (e) {
                        console.log('In FAIL:', e);
                    });
                }
            }
        }
    }).done(function (result) {
        console.log('Completed');
    }).fail(function (e) {
        console.log('FAIL:', e);
    });


    $('#delete_cluster_id').click(function () {
        alert('clicked - delete cluster - button');

        let selected_rows = gridOptions.api.getSelectedRows();
        if (!selected_rows) {
            alert('select atleast one row!');
            return false;
        }

        let selected_ids = selected_rows.map(function (each_row) {
            return each_row.id;
        });

        $.ajax({
            type: 'POST',
            url: window.origin + '/clusters_api/',
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            data: JSON.stringify({
                'action': 'delete',
                'selected_ids': selected_ids
            }),
            contentType: 'application/json;charset=utf-8',
            dataType: 'json',
            success: function (result) {
                console.log(' In Success')
            }
        }).done(function (result) {
            console.log('In Completed');
            alert('cluster deleted. Please reload the page');
            location.forcedReload(true);
        }).fail(function (e) {
            console.log('In FAIL:', e);
        });
    });

    $('#create_cluster_form_id').click(function () {
        console.log('clicked - create cluster - button');

        let cluster_name = document.getElementById('cluster_name_id').value;
        let nodes_count = document.getElementById('nodes_count_id').value;

        if (cluster_name && nodes_count) {
            $.ajax({
                type: 'CREATE',
                url: window.origin + '/clusters_api/',
                headers: {'X-CSRFToken': getCookie('csrftoken')},
                data: JSON.stringify({
                    'cluster_name': cluster_name,
                    'nodes_count': nodes_count,
                }),
                contentType: 'application/json;charset=utf-8',
                dataType: 'json',
                success: function (result) {
                    console.log(' In Success')
                }
            }).done(function (result) {
                console.log('In Completed');
                alert('New cluster created. Please reload the page');
                location.forcedReload(true);
            }).fail(function (e) {
                console.log('In FAIL:', e);
            });
        } else {
            alert('Invalid submission');
        }
    });
});