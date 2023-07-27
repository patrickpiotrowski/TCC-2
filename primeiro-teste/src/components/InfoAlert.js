import { Card } from "@mui/material"
import Alert from '@mui/material/Alert';

function InfoAlert({info, info2}){
    return(
        <>
            <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
                <Alert severity="info"> {info} </Alert>
            </Card>
            <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
                <Alert severity="warning"> {info2} </Alert>
            </Card>
        </>
    )
}

export default InfoAlert