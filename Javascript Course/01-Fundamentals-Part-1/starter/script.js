/* let js = "amazing";

// How we can access the console
console.log(40+5-8*2);
// --------------------------------------------------------------------------------------------
//  Values are pieces of data
// declaring a variable
let firstName = "Hassan";
let number = 50;
//  we can pass variables like this, diferent namings inclkude camelCase, which is standard int eh JS world, we can do first_name, names cannot start with a number pretty much like all the other langages we have used so far
// Note we use let as to provent data leaking or ither things access them when they shoudlnt be like declaring vairble ina n if statement or loop, fucntion etc
console.log(firstName);
firstName = 50;
console.log(firstName);
// Note make sure variable names are descriptive and that constants are upper()
// ##################################################################################################################################################################
// Values and Variables Assignment
let country = "Canada";
let continent = "North America";
let population = 37000000;
console.log(country);
console.log(continent);
console.log(population); 
// ##################################################################################################################################################################
let jsIsTheLang = true;
console.log(jsIsTheLang)
console.log(typeof jsIsTheLang) // this is how we can figure out what is the type of the value (note again the varaible does not have a type its the value that does)
// when we declare a new variable use let, when we reassign it there is no need for let
let und;
console.log(typeof und) // becuase we have not defined anything this means its type is undefined 
// ##################################################################################################################################################################
// Data Types Assignment
let isIsland = false
let language;
console.log(typeof isIsland)
console.log(typeof population)
console.log(typeof country)
console.log(typeof language)
// ##################################################################################################################################################################
// There are 3 ways to assign a variable

// use let for variables that can change later ie reassign a value
let age = 9
age = 10
// user const for varaibles that are not going to change in the future, infact we cannot change it, it will not let us
const birthYear = 1990
// birthYear = 1991 // this will cause an error
// const birthdy; // this will cause an error aswell

// there is also var, but we avoid using this
var job = "engineer" // works liek let but its not the same
// ##################################################################################################################################################################
// let, const, var Assignment
// gonna skip its really basic lol
// ##################################################################################################################################################################
const currentYear = 2037
const ageJonas = currentYear - 1991
const ageSarah = currentYear - 2018 // note we are using const here as these are years that do not change

console.log(ageJonas*2, ageSarah/2, 2**3) // the ** is the exponent operator 

// we can concatonate strings
const firstName = "Hassan"
const lastName = "Bahsoun"
console.log(firstName + " " + lastName) // there is a better way of doing this but rn just focuiong on operators

let x = 10 + 5;
console.log(x)
x +=1;
console.log(x)
x *= 5
console.log(x)
x ++ // increment by 1
console.log(x)
x-- // decrement by 1
console.log(x)
// comparison operators > < yield boolean results
console.log(10 < 20)
// ##################################################################################################################################################################
// Basic Operators Assignment
// gonna skip its really basic lol
// ##################################################################################################################################################################
// operator precedence
// google mdn operator prcedence: usually math operators are excuted before the comparison operatoers, bt also brackets precede everything 
// ##################################################################################################################################################################
// string and template literals (easy way to build string)
const firstName = "Hassan";
const job = "teacher";
const birthYear = 2002;

// we could it this way
const hassan = "I'm " + firstName + ", a " + (2025-birthYear) + " year old " + job
console.log(hassan)
// but template literals are better
const hassanNew = `I'm ${firstName}, a ${2025-birthYear} year old ${job}` // NOTE this is not quations
console.log(hassanNew) // this is a far better way of constructing our strings
console.log(`"Hello there" this is wwhat obi wan said`)
console.log(`this is the first line \nthis is the second line \n=this is the third line`)
// or we can do this
console.log(`this is the first line
this is the second line 
this is the third line`)
// ##################################################################################################################################################################
// if / else statements
const age  = 19
const isOldEnough = age >= 18

// this is called a control structure as its controls block of code and which will excute and which will not
if (isOldEnough){
    console.log("they are old enough to start driving")
}else{
    console.log(`they are not old enough to start driving, wait another ${18-age} years`)
}

const birthYear = 2012
let century;

if (birthYear <= 2000){
    century = 20
}else{
    century = 21
}

console.log(century)
// ##################################################################################################################################################################
// Type Conversion and Coercion

const year = `1991`
console.log(18+year) // this doesnt work we need a way of converting the string to an integer
console.log(18 + Number(year))

// Type coercion, behind the scenes if there are 2 types it will convert one to make it work
console.log(18+year) // like here between string and nunber the number will convert toa string

let n = "1" + 1
n = n -1
console.log(n) // should be 10
// ##################################################################################################################################################################
// Truthy and Falsy values
// thre are 5 falsy vlaues  -> 0, '', undefined, null, Nan
// all other values are truthy
console.log(Boolean(0))
console.log(Boolean(``))
console.log(Boolean(NaN))
console.log(Boolean(undefined))
console.log(Boolean(null))
console.log(Boolean(1))
console.log(Boolean("hello"))

const money = 10

if(money){
    console.log("Nice")
}else{
    console.log("You dont have money to spend")
}
// ##################################################################################################################################################################
// == vs ===, === is for both sides being exactly the same no type coersion, == is not strict and will do type coercion 
const age = 18
if(age === 18) console.log("Hey there")
if (age == "18") console.log("we did coercion here")
if (age === "18") console.log("this will not be printed")

const fav = prompt("What is your fav number? ")
console.log(typeof fav)

if (fav === 23){
    console.log("23 is a cool number")
} else if (fav === "7"){
    console.log("7 is a cool number")
}else if (Number(fav) === 9){
    console.log("9 is a cool number")
}else{
    console.log("wow you picked THE cool number")
}
// ##################################################################################################################################################################
// Logical Operators
const hasDriversLicense = true
const hasGoodVision = true

console.log(hasDriversLicense && hasGoodVision)
console.log(!hasDriversLicense && hasGoodVision)
console.log(hasDriversLicense && !hasGoodVision)
console.log(!hasDriversLicense && !hasGoodVision)
console.log("------------------------------------")
console.log(hasDriversLicense || hasGoodVision)
console.log(!hasDriversLicense || hasGoodVision)
console.log(hasDriversLicense || !hasGoodVision)
console.log(!hasDriversLicense || !hasGoodVision)

if (hasDriversLicense && hasGoodVision){
    console.log("Sarah is able to drive")
}else{
    console.log("someone else should drive")
}

const isTired = true

if (hasDriversLicense && hasGoodVision && !isTired){
    console.log("Sarah can drive")
}else{
    console("someone else should drive")
}
// ##################################################################################################################################################################  
// switch statments, when we want to see what value a variable has, like weekday is either sunday mnday tuesday wednesday etc
// easier to use a switch rather than an if

const day = prompt("What day is it")

switch(day){ // must indlcue a break becuase it will comstinue eecting down the structure
    case 'monday':
        console.log("math class")
        break;
    case 'tuesday':
        console.log("gym class")
        break
    case 'wednesday':
        console.log("comp class")
        break
    case 'thursday':
        console.log("english class")
        break
    case 'friday':
    case 'saturday':
        console.log("party")
        break
    case 'sunday':
        console.log("clean house")
        break
    default:
        console.log("that is not a valid day")
}*/
// ##################################################################################################################################################################  
// Statements (does not produce a value, performs some actions) and Expressions (a piece of code that produces a value like 3+4)     
// ##################################################################################################################################################################  
// Conditional operator 

const age = 23
// this is like doing an if else in one line like python print(...) if .. else print()
const activity = age >= 18 ? "I like to go to the casino" : "I like to play video games"
console.log(activity)

// these can be placed in a template literal 
console.log(`he said ${age >= 18 ? "I like to go to the casino" : "I like to play video games"}`)







