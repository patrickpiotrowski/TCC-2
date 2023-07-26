import avatar from '../findIconFull.png';
import UTFLogo from '../image.png';
import Card from '@mui/material/Card';
import { ImageList, ImageListItem, Stack } from '@mui/material';

function PresentationCard (){
    return(
        <Card sx={{ marginTop: '1rem', marginBottom: '1rem' }}>
        <Stack alignItems={'center'} direction="row" spacing={2}>
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
          <h1 style={{ margin: '1rem', textAlign: 'center', color: "#303030" }}>Ajuda para busca de orientador UTFPR-CP</h1>
          <h3 style={{ margin: '1rem', textAlign: 'justify', textJustify: 'initial', color: "#505050" }}>Se você está com dificuldades para encontrar um orientador, veio ao lugar certo!
            Esta plataforma foi desenvolvida para o Trabalho de Conclusão de Curso da UTFPR
            de Cornélio Procópio.</h3>
        </Stack>
      </Card>
    )
}

export default PresentationCard