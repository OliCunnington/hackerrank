

/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) 
{
     try 
     {
        var spl = s.split('')
        spl = spl.reverse()
        var outstr = spl.join('')
        console.log(outstr);
      } catch (e) 
     {
        console.log("s.split is not a function");
        console.log(s);
     }
}


