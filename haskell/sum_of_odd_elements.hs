f arr = sum (filter(\x -> x `mod` 2 == 1) arr)-- Fill up this function body

-- This part handles the Input/Output and can be used as it is. Do not change or modify it.
main = do
	inputdata <- getContents
	putStrLn $ show $ f $ map (read :: String -> Int) $ lines inputdata