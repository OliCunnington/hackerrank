-- Enter your code here. Read input from STDIN. Print output to STDOUT
import System.IO


unique :: String -> String
unique [] = []
unique (x:xs) = x : unique [y | y <- xs, y /= x]

main = do
    z <- getLine :: IO String
    putStrLn (unique z)
