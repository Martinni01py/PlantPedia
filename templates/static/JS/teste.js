

function marcarBotao(btnId) {
  // Remova a classe "active" de todos os botões
  $('.nav-link.botao').removeClass('active');

  // Adicione a classe "active" ao botão clicado
  $('#nav-link-' + btnId).addClass('active');

  // Oculte todas as divs adicionais
  $('.additional-div').hide();

  // Verifique qual botão foi clicado
  if (btnId === 1) {
    // Exiba a div "Info"
    $('#info-div').show();
  } else if (btnId === 2) {
    // Exiba a div "manutencao-div"
    $('#manutencao-div').show();
  } else if (btnId === 3) {
    // Exiba a div "historico-div"
    $('#historico-div').show();
  }
  else if (btnId === 4) {
    // Exiba a div "status-div"
    $('#status-div').show();
  }
}
