import * as React from 'react';
import { DataGrid, GridToolbar } from '@mui/x-data-grid';
import { useEffect } from 'react';

function TheDataGrid({ data, maxValues }) {
    const columns = [
        { field: 'id', headerName: 'ID', width: 50, sortable: false},
        { field: 'name', headerName: 'Professor', sortable: false, description: 'Essa coluna não é classificável.', width: 250 },
        { field: 'email', headerName: 'Email', sortable: false, description: 'Essa coluna não é classificável.', width: 200 },
        {
            field: 'title_distance',
            headerName: 'Dist. título',
            type: 'number',
            width: 100
        },
        {
            field: 'description_distance',
            headerName: 'Dist. descrição',
            type: 'number',
            width: 100
        },
        {
            field: 'mean',
            headerName: 'Média',
            description: 'Essa coluna não é classificável.',
            sortable: false,
            valueGetter: (params) => {
                return (((parseFloat(params.row.title_distance) + parseFloat(params.row.description_distance)) / 2).toFixed(5))
            },
            width: 100
        },
    ];

    const rows = data

    useEffect(() => {
        console.log(maxValues.title)
    }, [])

    
    // TODO: implementar o cálculo da média pra poder colocar na coluna (inserir a média em cada obj)


    return (
        <DataGrid
            rows={rows}
            columns={columns}
            initialState={{
                pagination: {
                    paginationModel: { page: 0, pageSize: 5 },
                },
                columns: {
                    columnVisibilityModel: {
                      id: false,
                    },
                },
                sorting: {
                    sortModel: [{ field: 'title_distance', sort: 'asc' }],
                },
            }}
            pageSizeOptions={[5, 10]}
            slots={{
                toolbar: GridToolbar,
              }}
        />
    )
}

export default TheDataGrid