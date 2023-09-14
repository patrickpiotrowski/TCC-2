import { Card } from "@mui/material"
import Alert from '@mui/material/Alert';
import { Button } from "@mui/material";
import Dialog from "@mui/material/Dialog";
import { useState, useEffect } from 'react';
import CardContent from '@mui/material/CardContent';

function InfoAlert({info, info2, info3, darkmode}){
    const [open, setOpen] = useState(false)
    const [dark, setDark] = useState(darkmode.darkMode)

    useEffect(() => {
        setDark(!darkmode)
    }, [darkmode]);

    const handleClick = () => {
        setOpen(true)
    }

    const handleClose = () => {
        setOpen(false)
    }

    return(
        <>
            <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
                <Alert severity="warning"> {info3}</Alert>
            </Card>
            <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
                <Alert severity="info"> {info} </Alert>
            </Card>
            <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
                <Alert severity="info"> {info2}<Button variant="text" size="small" onClick={handleClick}>clicando aqui</Button></Alert>
            </Card>
            <Dialog onClose={handleClose} open={open} maxWidth="md">
                <Card size="lg">
                    <CardContent>
                        <h1 style={{ margin: '1rem', textAlign: 'center', color: dark ? "#303030" : "#FFF" }}>As fórmulas consistem em:</h1>
                        <h2>% do título</h2>
                        <h4 style={{ margin: '1rem', textAlign: 'justify', textJustify: 'none', color: dark ? "#505050" : "#FFF" }}>100 - (100 * (DISTANCIA_TITULO_PROF - MENOR_DISTANCIA_TITULO_PROFS) / (MAIOR_DISTANCIA_TITULO_PROFS - MENOR_DISTANCIA_TITULO_PROFS))</h4>
                        <h2>% da descrição</h2>
                        <h4 style={{ margin: '1rem', textAlign: 'justify', textJustify: 'initial', color: dark ? "#505050" : "#FFF" }}>100 - (100 * (DISTANCIA_DESC_PROF - MENOR_DISTANCIA_DESC_PROFS) / (MAIOR_DISTANCIA_DESC_PROFS - MENOR_DISTANCIA_DESC_PROFS))</h4>
                        <h2>% da média</h2>
                        <h4 style={{ margin: '1rem', textAlign: 'justify', textJustify: 'none', color: dark ? "#505050" : "#FFF" }}>100 - ((%_TITULO + %_DESC)/2)</h4>
                    </CardContent>
                </Card>
            </Dialog>
        </>
    )
}

export default InfoAlert