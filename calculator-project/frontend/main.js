
new Vue({
    el: '#app',
    data: {
        numero1: null,
        numero2: null,
        operacao: 'soma',
        resultado: null
    },
    methods: {
        async calcular() {
            try {
                const response = await fetch('/api/calcular', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        operacao: this.operacao,
                        numero1: parseFloat(this.numero1),
                        numero2: parseFloat(this.numero2)
                    })
                });

                const data = await response.json();
                if (response.ok) {
                    this.resultado = data.resultado;
                } else {
                    alert(data.erro);
                }
            } catch (error) {
                console.log('Erro:', error);
            }
        }
    }
});
