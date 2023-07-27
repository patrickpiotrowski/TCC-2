import * as React from "react";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import { Box } from "@mui/material";
import Card from '@mui/material/Card';

function Footer() {
  return (
    <Card
      component="footer"
      sx={{
        backgroundColor: (theme) =>
          theme.palette.mode === "light"
            ? theme.palette.grey[200]
            : theme.palette.grey[800],
        marginTop: '1rem',
        marginBottom: '1rem'
      }}
      
    >
      <Container maxWidth="sm" sx={{padding: '1rem'}}>
        <Grid container spacing={5}>
          <Grid item xs={12} sm={6} align="left">
            <Typography variant="h6" color="text.primary" gutterBottom>
              Sobre
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Trabalho desenvolvido para o TCC de Engenharia de Computação da UTFPR - CP.
            </Typography>
          </Grid>
          <Grid item xs={12} sm={6} align="right">
            <Typography variant="h6" color="text.primary" gutterBottom>
              Contato
            </Typography>
            <Typography variant="body2" color="text.secondary">
              UTFPR
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Email: piotrowski@alunos.utfpr.edu.br
            </Typography>
          </Grid>
        </Grid>
        <Box mt={5}>
          <Typography variant="body1" color="text.secondary" align="center">
            {new Date().getFullYear()}
          </Typography>
        </Box>
      </Container>
    </Card>
  );
}

export default Footer