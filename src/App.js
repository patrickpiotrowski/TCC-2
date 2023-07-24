import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import SearchIcon from '@mui/icons-material/Search';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import { useState } from 'react';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';

import './App.css';
import { CardActions, CardHeader} from '@mui/material';

function App() {

  const [title, setTitle] = useState("")
  const [description, setDescription] = useState("")
  const [open, setOpen] = useState(false)
  const [errorMessage, setErrorMessage] = useState("")

  const validateInputs = () => {
    if (title.trim() === '' || description.trim() === '') {
      setErrorMessage("Uma ou mais entradas são inválidas!")
      setOpen(true)
    }
    else if (title.trim().length < 10 || description.trim().length < 20) {
      setErrorMessage("O título deve ter pelo menos 10 caracteres e a descrição deve ter ao menos 20 caracteres!")
      setOpen(true)
    }
  }

  const Alert = React.forwardRef(function Alert(props, ref) {
    return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
  });

  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpen(false);
  };

  return (
    <Container maxWidth="sm">
      <Card>
        <CardHeader title="Ajuda para busca de orientador"
          subheader="Se você está com dificuldades para encontrar um orientador, veio ao lugar certo!"/>

        <CardContent>
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextField fullWidth label='Titulo' required onChange={e => setTitle(e.target.value)}></TextField>
            </Grid>
            <Grid item xs={12}>
              <TextField fullWidth label='Descrição' required multiline minRows={5} onChange={e => setDescription(e.target.value)}></TextField>
            </Grid>
          </Grid>
        </CardContent>

        <CardActions sx={{ display: 'flex', flexDirection: 'row', justifyContent: 'flex-end', marginRight: '0.5rem'}}>
          <Button onClick={validateInputs} endIcon={<SearchIcon />} variant='contained'>
            Buscar
          </Button>
        </CardActions>

      </Card>

      <Snackbar open={open} autoHideDuration={3000} onClose={handleClose}
        anchorOrigin={{ vertical: "bottom", horizontal: "center" }} key="bottom center">
        <Alert severity='error' sx={{ width: '100%' }} onClose={handleClose}>
          {errorMessage}
        </Alert>
      </Snackbar>

    </Container>
  );
}

export default App;
