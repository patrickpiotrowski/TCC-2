import avatar from '../findIconFull.png';
import UTFLogo from '../image.png';
import Card from '@mui/material/Card';
import { ImageList, ImageListItem, Stack } from '@mui/material';
import { useState, useEffect } from 'react';

function PresentationCard (darkmode){
  const [dark, setDark] = useState(darkmode.darkMode)

  useEffect(() => {
    setDark(!darkmode.darkMode)
  }, [darkmode]);

    return(
        <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
        <Stack alignItems={'center'} direction="row" justifyContent={'center'} spacing={2}>
          <ImageList cols={2} sx={{margin: '1rem'}}>
            <ImageListItem>
              <img alt='' src={avatar} style={{width: '150px', height: '140px'}}></img>
            </ImageListItem>
            <ImageListItem>
              <img alt='' src={UTFLogo} style={{width: '350px', height: '100px'}}></img>
            </ImageListItem>
          </ImageList>
        </Stack>
        <Stack>
          <h1 style={{ margin: '1rem', textAlign: 'center', color: dark ? "#303030" : "#FFF" }}>Ajuda para busca de orientador UTFPR-CP</h1>
          <h3 style={{ margin: '1rem', textAlign: 'justify', textJustify: 'initial', color: dark ? "#505050" : "#FFF" }}>Se você cursa Engenharia de Computação na UTFPR-CP e está com dificuldades para encontrar um orientador, veio ao lugar certo!
            Esta plataforma foi desenvolvida para o Trabalho de Conclusão de Curso da UTFPR
            de Cornélio Procópio.</h3>
        </Stack>
      </Card>
    )
}

export default PresentationCard