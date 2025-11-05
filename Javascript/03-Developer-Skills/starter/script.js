// Remember, we're gonna use strict mode in all scripts now!
'use strict';

// prettier is now set up soooo, when you click ctrl save, prettier will format it prettier for us
// console.log('Hello world');

// for (let i = 0; i < 10; i++) {
//   console.log(i);
// }


const measureKelvin = function(){
    const measurement = {
        type: "temp",
        unit: "celcious",
        value: prompt("degrees celcius: ")

    }
    const kelvin = measurement.value +273
    return kelvin
}

console.log(measureKelvin())