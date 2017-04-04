function FizzBuzz(x){
	if (x%3==0 && x%5==0){
		return ('FizzBuzz\n');
	}
	else if (x%3==0){
		return ('Fizz\n');
	}
	else if (x%5==0){
		return ('Buzz\n');
	}
	else{
		return ('%d\n',x)
	}
}
