function usedHours(id){
  token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

  $.ajax({
    type: 'POST',
    url: '/overtime/used_overtime/' + id + '/',
    data: {
      csrfmiddlewaretoken: token
    },
    success: function(result){
      $('#mensagem').text(result.mensagem);
    }
  })
}