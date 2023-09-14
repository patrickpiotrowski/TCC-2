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
import Alert from '@mui/material/Alert';
import Checkbox from '@mui/material/Checkbox';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import CircularProgress from '@mui/material/CircularProgress';
import { CardActions } from '@mui/material';
import HighlightOffIcon from '@mui/icons-material/HighlightOff';
import InputAdornment from '@mui/material/InputAdornment';
import IconButton from '@mui/material/IconButton';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import FormControl from '@mui/material/FormControl';

import axios from 'axios'

import './App.css';

import PresentationCard from './components/PresentationCard';
import TheDataGrid from './components/TheDataGrid';
import TheFooter from './components/TheFooter';
import InfoAlert from './components/InfoAlert';

import { ThemeProvider, CssBaseline } from '@mui/material';
import { lightTheme, darkTheme } from './theme';
import Brightness4Icon from '@mui/icons-material/Brightness4';

function App() {
  const information = "Veja que a tabela está classificada da melhor correspondência do título para a menor. Caso queira, pode trocar a organização da tabela utilizando os botões junto ao cabeçalho."
  const information2 = "Caso queira saber o como a porcentagem da correnspondência é calculada, você pode ver as fórmulas"
  const information3 = "100% de correspondência NÃO significa que o professor é totalmente compatível, mas sim que, dentre as opções, essa é a melhor calculada pelo algorítmo."

  const [answer, setAnswer] = useState()
  const [answerMax, setAnswerMax] = useState()
  const [answerMin, setAnswerMin] = useState()
  const [title, setTitle] = useState("Desenvolvimento de um Sistema de Reconhecimento de Gestos para Controle de Dispositivos Eletrônicos")
  const [description, setDescription] = useState("Este trabalho de conclusão de curso em Engenharia de Computação explora o desenvolvimento de um sistema inovador de reconhecimento de gestos que permite aos usuários controlar dispositivos eletrônicos, como smartphones e computadores, por meio de gestos corporais. O estudo abrange desde a concepção e implementação do sistema até sua avaliação de desempenho e potenciais aplicações em diversas áreas, destacando-se como uma solução promissora para melhorar a interação homem-máquina e tornar a tecnologia mais acessível e intuitiva")
  const [openError, setOpenError] = useState(false)
  const [openSuccess, setOpenSuccess] = useState(false)
  const [errorMessage, setErrorMessage] = useState("")
  const [successMessage, setSuccessMessage] = useState("")
  const [timeTaken, setTimeTaken] = useState()
  const [checked, setChecked] = useState(false)
  const [running, setRunning] = useState(false)
  const [model, setModel] = useState('')
  const [modelsArray, setModelsArray] = useState([])
  const [darkMode, setDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const validateInputs = () => {
    if (title.trim() === '' || title.trim().length < 10) {
      setErrorMessage("O título deve ter mais de 10 caracteres!")
      setOpenError(true)
    }
    else if (description.trim() === '' || description.trim().length < 20) {
      setErrorMessage("A descrição deve ter ao menos 20 caracteres!")
      setOpenError(true)
    }
    else if (model === '') {
      setErrorMessage("Você deve escolher um modelo!")
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
    getModels()
    if (answer) {
      handlePercetage()
    }
  }, [answer]);

  const makeRequest = () => {
    const id = new Date().getTime()
    const obj = {
      "id": id,
      "title": title,
      "description": description,
      "model": model
    }
    setRunning(true)
    setTimeTaken()
    setAnswer()
    axios.post("http://127.0.0.1:8000/items/{item.id}", obj)
      .then(function (response) {
        setAnswer(response.data[0])
        setAnswerMax(response.data[1])
        setAnswerMin(response.data[2])
        resetInputs()
        const timeTaken = response.data[3].timeTaken
        const min = Math.floor(timeTaken / 60)
        const sec = Math.floor(timeTaken % 60)
        setSuccessMessage(`Tudo certo!`)
        setTimeTaken(`Tempo decorrido: ${min} ${min > 1 ? 'minutos' : 'minuto'} e ${sec} ${sec > 1 ? 'segundos' : 'segundo'}`)
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
    setDescription('')
    setTitle('')
    setModel('')
  }

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

  const handlePercetage = () => {
    for (var key in answer) {
      var professor = answer[key]

      professor.title_distance = Number(professor.title_distance)
      professor.description_distance = Number(professor.description_distance)
      answerMin.title = Number(answerMin.title)
      answerMax.title = Number(answerMax.title)

      const percentage_title = 100 * (professor.title_distance - answerMin.title) / (answerMax.title - answerMin.title)
      const percentage_desc = 100 * (professor.description_distance - answerMin.description) / (answerMax.description - answerMin.description)

      professor.title_distance = 100 - percentage_title.toFixed(2)
      professor.description_distance = 100 - percentage_desc.toFixed(2)

      professor.mean = 100 - ((percentage_title + percentage_desc) / 2).toFixed(2)
      professor.mean = Number(professor.mean)
    }
  }

  const resetTitleInput = () => {
    setTitle('')
  }

  const resetDescInput = () => {
    setDescription('')
  }

  const handleModel = (event) => {
    setModel(event.target.value);
  };

  const getModels = () => {
    axios.get('http://127.0.0.1:8000/models')
      .then((response) => {
        for (let i = 0; i < response.data.length; i++) {
          response.data[i] = response.data[i].split('.')[0]
        }
        setModelsArray(response.data)
      })
      .catch((error) => {
        console.log('Erro ao pegar os modelos!' + JSON.stringify(error))
      })
  }

  const generateModelMenu = () => {
    // sorting the array
    modelsArray.sort((a, b) => {
      const numA = parseInt(a.match(/\d+/)[0]);
      const numB = parseInt(b.match(/\d+/)[0]);
      return numA - numB;
    });

    let optionsArray = []
    for (let i in modelsArray) {
      let option = modelsArray[i]
      let dimension = option.split('s')[1]
      let name = option.split('_')[0]
      name = name.toUpperCase()
      optionsArray.push(<MenuItem key={i} value={option}>{name} com {dimension} dimensões</MenuItem>)
    }
    return optionsArray
  }

  return (
    <ThemeProvider theme={darkMode ? darkTheme : lightTheme}>
      <CssBaseline />
      <div className="App">
        <Container maxWidth="md">
        <div style={{display: "flex", alignItems: "center", justifyContent: "flex-end"}}>
          <IconButton onClick={toggleDarkMode}>
            <Brightness4Icon />
          </IconButton>
        </div>
          <PresentationCard darkMode={darkMode}/>
          <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
            <CardContent>
              <Grid container spacing={2}>
                <Grid item xs={12}>
                  <TextField fullWidth disabled={running ? true : false} label='Titulo' value={title} required onChange={e => setTitle(e.target.value)} InputProps={{
                    endAdornment:
                      <InputAdornment position="end">
                        <IconButton onClick={resetTitleInput}>
                          <HighlightOffIcon />
                        </IconButton>
                      </InputAdornment>,
                  }}>
                  </TextField>
                </Grid>
                <Grid item xs={12}>
                  <TextField fullWidth disabled={running ? true : false} label='Descrição' value={description} required multiline minRows={5} onChange={e => setDescription(e.target.value)} InputProps={{
                    endAdornment:
                      <InputAdornment position="end">
                        <IconButton onClick={resetDescInput}>
                          <HighlightOffIcon />
                        </IconButton>
                      </InputAdornment>,
                  }} >

                  </TextField>
                </Grid>
                <Grid item xs={6}>
                  <FormControl fullWidth disabled={running ? true : false}>
                    <InputLabel>Modelo</InputLabel>
                    <Select
                      value={model}
                      label="Modelo"
                      onChange={handleModel}
                    >
                      {modelsArray.length > 0 ?
                        generateModelMenu()
                        : null
                      }
                    </Select>
                  </FormControl>
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
              {
                answer ?
                  <p style={{ color: 'rgb(255, 0 ,0)', margin: '10px' }}>{timeTaken}</p>
                  :
                  null
              }
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

          {
            running ?
              <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
                <Alert severity="warning">Isso pode demorar um pouco, tenha paciência e não feche a página</Alert>
              </Card>
              :
              null
          }

          {
            answer ?
              <>
                <InfoAlert info={information} info2={information2} info3={information3} darkmode={darkMode}></InfoAlert>
                <TheDataGrid data={answer} maxValues={answerMax} />
              </>
              :
              null
          }

          <TheFooter></TheFooter>

          <Snackbar open={openError} autoHideDuration={4000} onClose={handleClose}
            anchorOrigin={{ vertical: "top", horizontal: "right" }} key="error">
            <Alert severity='error' sx={{ width: '100%' }} elevation={6} variant="filled" onClose={handleClose}>
              {errorMessage}
            </Alert>
          </Snackbar>

          <Snackbar open={openSuccess} autoHideDuration={4000} onClose={handleClose}
            anchorOrigin={{ vertical: "top", horizontal: "right" }} key="success">
            <Alert severity='success' sx={{ width: '100%' }} elevation={6} variant="filled" onClose={handleClose}>
              {successMessage}
            </Alert>
          </Snackbar>

        </Container>
      </div>
    </ThemeProvider>
  );
}

export default App;
