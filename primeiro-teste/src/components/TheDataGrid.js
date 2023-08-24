import * as React from 'react';
import { DataGrid, GridToolbar } from '@mui/x-data-grid';
import { Card } from '@mui/material';


function TheDataGrid({ data, maxValues }) {
    const columns = [
        { field: 'id', headerName: 'ID', width: 50, sortable: false },
        { field: 'name', headerName: 'Professor', sortable: false, description: 'Essa coluna não é classificável.', width: 250 },
        { field: 'email', headerName: 'Email', sortable: false, description: 'Essa coluna não é classificável.', width: 250 },
        {
            field: 'title_distance',
            headerName: ' % Título',
            type: 'number',
            width: 200
        },
        {
            field: 'description_distance',
            headerName: '% Descrição',
            type: 'number',
            width: 200
        },
        {
            field: 'mean',
            headerName: '% Média',
            type: 'number',
            width: 200
        },
    ];

    const rows = data

    return (
        <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
            <DataGrid
                rows={rows}
                columns={columns}
                initialState={{
                    pagination: {
                        paginationModel: { page: 0, pageSize: 10 },
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
                pageSizeOptions={[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]}
                slots={{
                    toolbar: GridToolbar,
                }} 
                />
        </Card>
    )
}

export default TheDataGrid