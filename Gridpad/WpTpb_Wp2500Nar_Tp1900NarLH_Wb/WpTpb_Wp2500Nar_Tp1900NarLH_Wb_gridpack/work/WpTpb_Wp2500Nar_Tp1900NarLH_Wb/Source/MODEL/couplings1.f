ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_44 = (MDL_COMPLEXI*MDL_GRHOPT23LBL)/MDL_SQRT__2
      GC_49 = (MDL_COMPLEXI*MDL_GRHOPUD)/MDL_SQRT__2
      GC_64 = (MDL_COMPLEXI*MDL_GWT23LBL)/MDL_SQRT__2
      END
