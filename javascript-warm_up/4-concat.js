#!/usr/bin/node

if(process.argv.length -2 === 0){
	console.log('No argument');
}
else {
	console.log(process.argv[2]+' is '+process.argv[3]);
}
