import Codec.Picture

main :: IO()
main = do
	image <- readImage "./Nintendo_Characters.png"
	case image of 
		Left e ->
			PutStrLn e
		Right dynamicImage ->
			saveGifImage './Nintendo_Characters.gif' dynamicImage