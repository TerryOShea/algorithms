function digitalRoot(num) {
  while (num >= 10) {
    num = sumNumDigits(num)
  }
  return num;
}

function sumNumDigits(num) {
  let sum = 0;
  while (num) {
    sum += num % 10;
    num = Math.floor(num/10);
  }
  return sum;
}

function caesarCipher(str, shift) {
  return str.split("").map(char => shiftChar(char, shift)).join("");
}

function shiftChar(char, shift) {
  if (char.match(/[a-z]/)) {
    return String.fromCharCode(((char.charCodeAt() - 97 + shift) % 26) + 97);
  } else if (char.match(/[A-Z]/)) {
    return String.fromCharCode(((char.charCodeAt() - 65 + shift) % 26) + 65);
  } else {
    return char;
  }
}

// LEARNED: "c".charCodeAt()
// LEARNED: "A" in ASCII is 65
// LEARNED: str.match(/[a-z]/i)
// LEARNED: String.fromCharCode(65)

function longestCommonSubstring(str1, str2) {
  const matrix = makeMatrix(str1, str2);
  let longestCommonSubstring = "";

  for (let i = 0; i < str1.length; i++) {
    for (let j = 0; j < str2.length; j++) {
      const lengthHere = matrix[i+1][j+1]
      if (lengthHere > longestCommonSubstring.length) {
        longestCommonSubstring = str2.slice(j - lengthHere + 1, j + 1);
      }
    }
  }

  return longestCommonSubstring;
}

function zero2d(rows, cols) {
  const array = [], row = [];
  while (cols--) row.push(0);
  while (rows--) array.push(row.slice());
  return array;
}

function makeMatrix(str1, str2) {
  const matrix = zero2d(str1.length + 1, str2.length + 1);

  for (let i = 0; i < str1.length; i++) {
    for (let j = 0; j < str2.length; j++) {
      if (str1[i] === str2[j]) {
        matrix[i+1][j+1] = matrix[i][j] + 1;
      }
    }
  }

  return matrix;
}

// LEARNED: best way to make a 2D array of zeros

function sumRec(arr) {
  if (arr.length === 0) return null;
  if (arr.length === 1) return arr[0];
  return arr[0] + sumRec(arr.slice(1));
}

function fibs(n) {
  if (n < 1) return null;
  if (n === 1) return [0];

  const fibs = [0, 1];

  let counter = 2;
  while (counter < n) {
    fibs.push(fibs[counter - 1] + fibs[counter - 2]);
    counter += 1;
  }

  return fibs;
}

function recursiveFibs(n) {
  if (n < 1) return null;
  if (n === 1) return [0];
  if (n === 2) return [0, 1];
  const prevFibs = recursiveFibs(n - 1);
  const newFib = prevFibs[prevFibs.length - 1] + prevFibs[prevFibs.length - 2];
  return [...prevFibs, newFib];
}

function isPalindrome(str) {
  for (let i = 0; i < Math.floor(str.length); i++) {
    if (str[i] !== str[str.length - i - 1]) {
      return false;
    }
  }
  return true;
}

function validIp(str) {
  if (!(str.match(/^\d+\.\d+\.\d+\.\d+$/))) return false;
  return str.split(".").every(el => parseInt(el) <= 255);
}

// LEARNED: str.match(/^\d+\.$/)

function sumFromFile(filename) {
  
}
