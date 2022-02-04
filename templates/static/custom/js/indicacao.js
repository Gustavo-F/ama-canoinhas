var csrftoken = Cookies.get('csrftoken');

function excluir_indicacao(pk) {
    if (confirm('Deseja realmente excluir esta indicação?')) {
        $.ajax({
            type: 'post',
            url: '/excluir_indicacao/' + pk,
            data: { csrfmiddlewaretoken: csrftoken, },
            dataType: 'json',
            success: function (response) {
                $('#indicacao_' + pk).remove();
            },
        });
    }
}