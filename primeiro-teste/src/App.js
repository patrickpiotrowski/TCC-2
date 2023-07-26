import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import SearchIcon from '@mui/icons-material/Search';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import { useState, useEffect } from 'react';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import Checkbox from '@mui/material/Checkbox';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import CircularProgress from '@mui/material/CircularProgress';
import { CardActions } from '@mui/material';

import axios from 'axios'

import './App.css';

import PresentationCard from './components/PresentationCard';

function App() {

  const [answer, setAnswer] = useState()
  const [title, setTitle] = useState("")
  const [description, setDescription] = useState("")
  const [openError, setOpenError] = useState(false)
  const [openSuccess, setOpenSuccess] = useState(false)
  const [errorMessage, setErrorMessage] = useState("")
  const [successMessage, setSuccessMessage] = useState("")
  const [checked, setChecked] = useState(false)
  const [running, setRunning] = useState(false)

  const validateInputs = () => {
    if (title.trim() === '' || title.trim().length < 10) {
      setErrorMessage("O título deve ter mais de 10 caracteres!")
      setOpenError(true)
    }
    else if (description.trim() === '' || description.trim().length < 20) {
      setErrorMessage("A descrição deve ter ao menos 20 caracteres!")
      setOpenError(true)
    }
    else if (checked !== true) {
      setErrorMessage("Você deve concordar com o termo!")
      setOpenError(true)
    }
    else {
      makeRequest()
    }
  }

  useEffect(() => {
    console.log("Deu boa! : " + JSON.stringify(answer));
  }, [answer]);

  const makeRequest = () => {
    const id = new Date().getTime()
    const obj = {
      "id": id,
      "title": title,
      "description": description
    }
    setRunning(true)
    axios.post("http://127.0.0.1:8000/items/{item.id}", obj)
      .then(function (response) {
        setAnswer(response.data)
        resetInputs()
        setSuccessMessage("Tudo certo!")
        setOpenSuccess(true)
        setRunning(false)
      })
      .catch((error) => {
        console.log("Deu ruim! : " + JSON.stringify(error))
        setErrorMessage("Ops! Algo deu errado! Por favor, tente novamente.")
        setRunning(false)
      })
  }

  const resetInputs = () => {
    setChecked(false)
    setDescription("")
    setTitle("")
  }

  const Alert = React.forwardRef(function Alert(props, ref) {
    return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />
  })

  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return
    }
    setOpenError(false)
    setOpenSuccess(false)
  }

  const handleChecked = (event) => {
    setChecked(!checked)
  }

  const handleIcon = () => {
    if (running) {
      return null
    }
    else {
      return <SearchIcon />
    }
  }

  const disableButton = () => {
    if (running) {
      return 'disabled'
    }
    else {
      return null
    }
  }

  // link do icone https://icons8.com.br/icon/nWljDzRch4Az/find

  return (
    <Container maxWidth="sm">

      <PresentationCard/>

      <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
        <CardContent>
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextField fullWidth disabled={running ? true : false} label='Titulo' value={title} required onChange={e => setTitle(e.target.value)}></TextField>
            </Grid>
            <Grid item xs={12}>
              <TextField fullWidth disabled={running ? true : false} label='Descrição' value={description} required multiline minRows={5} onChange={e => setDescription(e.target.value)}></TextField>
            </Grid>
            <Grid item xs={12}>
              <FormGroup>
                <FormControlLabel disabled={running ? true : false} required control={<Checkbox checked={checked} onChange={handleChecked} />}
                  label="Concordo em compartilhar os dados inseridos na plataforma para fins de estudo e validação." />
              </FormGroup>
            </Grid>
          </Grid>
        </CardContent>

        <CardActions sx={{ display: 'flex', flexDirection: 'row', justifyContent: 'flex-end', marginRight: '0.5rem' }}>
          <Button onClick={validateInputs} disabled={running ? true : false} endIcon={handleIcon()} {...disableButton} variant='contained'>
            {
              running ?
                <CircularProgress color='primary' />
                :
                'Buscar'
            }
          </Button>
        </CardActions>

      </Card>

      <Card>
        {
          answer ?
          <div>
            <p>Nome: {answer.nome}</p> 
            <p>Email: {answer.email}</p>
          </div>
          :
          null          
        }
      </Card>

      <Snackbar open={openError} autoHideDuration={4000} onClose={handleClose}
        anchorOrigin={{ vertical: "top", horizontal: "right" }} key="error">
        <Alert severity='error' sx={{ width: '100%' }} onClose={handleClose}>
          {errorMessage}
        </Alert>
      </Snackbar>

      <Snackbar open={openSuccess} autoHideDuration={4000} onClose={handleClose}
        anchorOrigin={{ vertical: "top", horizontal: "right" }} key="success">
        <Alert severity='success' sx={{ width: '100%' }} onClose={handleClose}>
          {successMessage}
        </Alert>
      </Snackbar>

    </Container>
  );
}

export default App;
