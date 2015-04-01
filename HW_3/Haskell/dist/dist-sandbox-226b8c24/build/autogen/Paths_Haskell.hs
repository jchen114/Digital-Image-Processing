module Paths_Haskell (
    version,
    getBinDir, getLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
catchIO = Exception.catch


version :: Version
version = Version {versionBranch = [0,1,0,0], versionTags = []}
bindir, libdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "T:\\Dropbox\\FLORIDA POLY\\Digital Image Processing\\HW_3\\Haskell\\.cabal-sandbox\\bin"
libdir     = "T:\\Dropbox\\FLORIDA POLY\\Digital Image Processing\\HW_3\\Haskell\\.cabal-sandbox\\x86_64-windows-ghc-7.8.3\\Haskell-0.1.0.0"
datadir    = "T:\\Dropbox\\FLORIDA POLY\\Digital Image Processing\\HW_3\\Haskell\\.cabal-sandbox\\x86_64-windows-ghc-7.8.3\\Haskell-0.1.0.0"
libexecdir = "T:\\Dropbox\\FLORIDA POLY\\Digital Image Processing\\HW_3\\Haskell\\.cabal-sandbox\\Haskell-0.1.0.0"
sysconfdir = "T:\\Dropbox\\FLORIDA POLY\\Digital Image Processing\\HW_3\\Haskell\\.cabal-sandbox\\etc"

getBinDir, getLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "Haskell_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "Haskell_libdir") (\_ -> return libdir)
getDataDir = catchIO (getEnv "Haskell_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "Haskell_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "Haskell_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "\\" ++ name)
