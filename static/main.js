var app = new Vue({
    el: '#app',
    data: {
        joinGameLobbyId: '',
        phoneNumber: '',
    },
    delimiters: ['[[', ']]'],
    methods: {
        createNewGame: function (event) {
            //
        },

        joinGame: function (event) {
            if (this.joinGameLobbyId.length == 6 && this.phoneNumber.trim() != '') {
                console.log('joining game: ' + this.joinGameLobbyId)

                let params = {
                    lobbyId: this.joinGameLobbyId,
                    phoneNumber: this.phoneNumber
                }

                fetch( 'http://localhost:5000/joinLobby', {method: 'POST',  body: JSON.stringify( params )})
                .then( response => response.json() )
                .then( response => {
                    console.log(response)
                } );
            }
        }
    }
})