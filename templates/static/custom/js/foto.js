var csrftoken = Cookies.get('csrftoken');

function excluir_foto_produto(pk) {
    if (confirm('Deseja realmente excluir esta foto?')) {
        $.ajax({
            type: 'post',
            url: '/excluir_foto_produto/' + pk,
            data: { csrfmiddlewaretoken: csrftoken, },
            dataType: 'json',
            success: function (response) {
                $('#foto_' + pk).remove();
            },
        });
    }
}