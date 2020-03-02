// Implementation with Express

var express = require('express');
var graphqlHTTP = require('express-graphql');
var { buildSchema } = require('graphql');

var app = express();    // create express server named app

app.use("/graphql", graphqlHTTP({
    schema: schema,
    rootValue: resolver
}));    // Now we are ready to handle /graphql requests

// Here "pizza_buns" is the name of method for requests
// "type PizzaBun" is for READ - used together with "type Query"
// "pizza_buns(pd_idx: Int)": to get a single PizzaBun whose id is pd_idx.
// "input PizzaBunInput" is for CREATE (Here we do not need pb_idx in post query) - used together with "type Mutation"
var schema = buildSchema(`

    type Query {
        pizza_buns: [PizzaBun]
        pizza_buns(pd_idx: Int): PizzaBun
    }

    type Mutation {
        create_pizza_bun(input: PizzaBunInput): Int
    }

    type PizzaBun {
        pb_idx: ID,
        pb_name: String,
        size: Int,
        bread: String,
        sauce: String,
        topping: String
    }

    input PizzaBunInput {
        pb_name: String,
        size: Int,
        bread: String,
        sauce: String,
        topping: String
    }
`)

// hard-coded version
var resolver = {
    pizza_buns: () => {
        return [ {
            "pd_idx": "1",
            "pd_name": "sausage",
            "size": 6,
            "bread": "wheat",
            "sauce": "tomato",
            "topping": "sausage"
        }, {
            "pd_idx": "2",
            "pd_name": "vegetable",
            "size": 7,
            "bread": "ciabatta",
            "sauce": "rose",
            "topping": "olive"
        }, {
            "pd_idx": "3",
            "pd_name": "seafood",
            "size": 7,
            "bread": "italian",
            "sauce": "arrabiata",
            "topping": "shirimp"
        } ]
    }
}

// MySQL query version
var resolver = {
    pizza_buns: async () => {
        return await new Promise((resolve) => {
            pool.getConnection(function(err, connection) {
                connection.query(
                    'SELECT * FROM pizza_bun',
                    (err, results) => {
                        connection.release();
                        if (err) throw err;
                        resolve(results);
                    }
                )
            })
        });
    },

    pizza_buns: async ({pd_idx}) => {
        return await new Promise((resolve) => {
            pool.getConnection(function(err, connection) {
                connection.query(
                    'SELECT * FROM pizza_bun WHERE pd_idx = ?',
                    [pd_idx],
                    (err, results) => {
                        connection.release();
                        if (err) throw err;
                        resolve(results[0]);
                    }
                )
            })
        })
    },

    create_pizza_bun: async ({input}) => {
        const insertResultData = await new Promise((resolve) => {
            pool.getConnection(function(err, connection) {
                connection.query(
                    'INSERT INTO pizza_bun (pb_name, size, bread, sauce, topping)'
                    + ' VALUES (?, ?, ?, ?, ?)',
                    [input.pb_name, input.size, input.bread, input.sauce, input.topping],
                    (err, results, fields) => {
                        connection.release();
                        if (err) throw err;
                        resolve(results);
                    }
                )
            })
        })
        return { pd_idx: insertResultData.insertId }
    },
}
