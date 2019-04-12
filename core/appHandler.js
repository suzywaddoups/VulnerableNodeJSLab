var db = require('../models')

var serialize = require("node-serialize")
const Op = db.Sequelize.Op

module.exports.userSearch = function (req, res) {
	var query = "SELECT login,name FROM Users WHERE login='" + req.body.login + "'";
	db.sequelize.query(query, {
		model: db.User
	}).then(user => {
		if (user.length) {
			var output = {
				user: {
					login: user[0].login,
					name: user[0].name,

				}
			}
			res.render('usersearch', {
				output: output
			})
		} else {
      console.log('Not found');
			req.flash('warning', 'User not found')
			res.render('usersearch', {
				output: null
			})
      console.log('in else');
		}
	}).catch(err => {
		req.flash('danger', 'Internal Error')
		res.render('usersearch', {
			output: null
		})
	})
}

module.exports.listProducts = function (req, res) {
	db.Product.findAll().then(products => {
		output = {
			products: products
		}
		res.render('products', {
			output: output
		})
	})
}

module.exports.productSearch = function (req, res) {
	db.Product.findAll({
		where: {
			name: {
				[Op.like]: '%' + req.body.name + '%'
			}
		}
	}).then(products => {
		output = {
			products: products,
			searchTerm: req.body.name
		}
		res.render('products', {
			output: output
		})
	})
}

module.exports.redirect = function (req, res) {
	if (req.query.url) {
		res.redirect(req.query.url)
	} else {
		res.send('invalid redirect url')
	}
}
