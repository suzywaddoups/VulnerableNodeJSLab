var router = require('express').Router()
var appHandler = require('../core/appHandler')



module.exports = function () {
    router.get('/', function (req, res) {
        res.render('index')
    })

    //User Search
    router.get('/usersearch', function (req, res) {
        res.render('usersearch', {
            output: null
        })
    })

    router.post('/usersearch', appHandler.userSearch)

    //Products
    router.get('/products', appHandler.listProducts)

    router.post('/products', appHandler.productSearch)

    return router
}
