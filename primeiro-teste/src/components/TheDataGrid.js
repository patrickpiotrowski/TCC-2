import * as React from 'react';
import { DataGrid, GridToolbar } from '@mui/x-data-grid';
import { Card } from '@mui/material';


function TheDataGrid({ data, maxValues }) {
    const columns = [
        { field: 'id', headerName: 'ID', width: 50, sortable: false },
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
            type: 'number',
            width: 100
        },
    ];

    const rows = data

    // TODO: implementar o cálculo da média pra poder colocar na coluna (inserir a média em cada obj)


    return (
        <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
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
        </Card>
    )
}

export default TheDataGrid