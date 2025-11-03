// activating scrict mode = makes it easier for us to write secure js code, avoids errors, makes erros visible some of them, and forbids us from doing certain things
'use strict';// must be the very first statement in the entire js script

// let hasDriversLicence = false;
// let passTest = true;
// if(passTest) hasDriversLicence = true;
// if (hasDriversLicence) console.log("I can drive")
// const interfacse = "audio"
// ===========================================================================================================================

// function logger(){
//     console.log("My Name is Jonas")
// }
// // this is how we call/ run/ invoke a function
// logger()
// logger()
// logger()

// // functions can pass data, and also return data back to us
// function fruitProcessor(apples, oranges){
//     console.log(apples, oranges)
//     const juice = `Juice with ${apples} apples, and ${oranges} oranges`
//     return juice
// }

// let juiceMade = fruitProcessor(3,2)
// console.log(juiceMade)

// juiceMade = fruitProcessor(0,5)
// console.log(juiceMade)
// ===========================================================================================================================
// // parameter is the placeholder, the arguments is what replaces that place holder in the case below borthyear is parameter, argument is 2002 
// // function declaration (we are allowd to call these functions before we actually even declare them)
// function calcAge1(birthyear){
//     return 2025-birthyear
// }
// const age = calcAge1(2002)

// // function expression (not allowed to use unless this is declared)
// const calAge2 = function (birthyear){
//     return 2025-birthyear
// }
// const age2 = calAge2(2002)
// console.log(age, age2)

// ===========================================================================================================================
// // arrow functions - 
// const calcAge3 = birthYear => 2025-birthYear
// console.log(calcAge3(2008))

// // if you want to pass multiple parameters just wrap them in a bracket
// const yearsUntilRetirement = birthYear =>{
//     const age = 2025- birthYear
//     const retirement = 65-age
//     return retirement
// }
// console.log(yearsUntilRetirement(2002))
// ===========================================================================================================================
// // calling functions with other functions

// function cutFruitPieces(fruit){
//     return fruit*4
// }

// function fruitProcessor(apples, oranges){
//     const applePieces = cutFruitPieces(apples)
//     const orangePieces = cutFruitPieces(oranges)

//     const juice = `Juice with ${applePieces} pieces of apple, and ${orangePieces} pieces or orange`
//     return juice
// }

// const juiceMade = fruitProcessor(5,3)
// console.log(juiceMade)
// ===========================================================================================================================
// //Arrays
// const friends = ['micheal', 'steven', 'peter']
// console.log(friends)

// const friends2 = ['peter','micheal', 'steven', 4, 5, true]
// console.log(friends2)

// const friend2 = 'micheal'
// const friend1 =  'steven'
// const friend3 = 'peter'
// const friends3 = [friend1,friend2,friend3]
// console.log(friends3)

// console.log(friends[0])
// console.log(friends2.length)
// console.log(friends[friends.length-1])

// friends2[friends2.length-1] = "Hassan"
// console.log(friends2)
// ===========================================================================================================================
// // Array Methods
// const friends = ['micheal', 'steven', 'peter']
// console.log(friends)
// // push adds elemetns to the end of the array
// const new_length = friends.push("Hassan") // we usually dont need this but it is somehting that push returns
// console.log(friends, new_length)
// // unshift adds elements tot he beginning of an array
// friends.unshift("Hassan") // we usually dont need this but it is somehting that push returns
// console.log(friends, new_length)
// // remove elements from the end of the list
// const elementPopped = friends.pop() 
// console.log(friends, elementPopped)
// // shift uis how we remove the fisrt element
// friends.shift() 
// console.log(friends)
// // get the index an element is located at
// console.log(friends.indexOf("peter"))
// // includes returns true or false if the param is in the array
// console.log(friends.includes("peter"))
// ===========================================================================================================================
// Objects
// object (literal since we write everything) in js are basically like dictionaries in python
// const jonas = {
//     firstName: "jonas",
//     lastName: "brother",
//     age: 23,
//     gender:"male",
//     friends: ['micheal', 'steven', 'peter']
// }
// // dot notation vs bracket notation
// console.log(jonas.lastName)
// console.log(jonas["lastName"])

// // can add to objects
// jonas.location = "Canada"
// jonas["twitter"] = "dont have one"
// console.log(jonas)

// console.log(`${jonas.firstName} has ${jonas.friends.length} friends, and his best friend is ${jonas.friends[0]}`)
// ===========================================================================================================================
// // object methods
// const jonas = {
//     firstName: "jonas",
//     lastName: "brother",
//     birthYear:2002,
//     gender:"male",
//     friends: ['micheal', 'steven', 'peter'],

//     calcAge: function (){
//         this.age=  2025-this.birthYear
//     }
// }
// jonas.calcAge()
// console.log(jonas.age)



