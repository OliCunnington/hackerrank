f :: [Int] -> [Int]
f [] = []
f [a, b] = [b]
f lst = [(head (tail lst))] ++ f (tail (tail lst))-- Fill up this Function

-- This part deals with the Input and Output and can be used as it is. Do not modify it.
main = do
	inputdata <- getContents
	mapM_ (putStrLn. show). f. map read. lines $ inputdata