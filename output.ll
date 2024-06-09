; ModuleID = "D:\Курсач (всё плохо)\pa\codegen.py"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define void @"main"()
{
entry:
  %"result" = alloca i32
  store i32 0, i32* %"result"
  %"numb" = alloca i32
  store i32 6, i32* %"numb"
  %".4" = load i32, i32* %"numb"
  %".5" = icmp ne i32 %".4", 0
  br i1 %".5", label %"if", label %"else"
if:
  %".7" = load i32, i32* %"result"
  %".8" = icmp eq i32 %".7", 0
  br i1 %".8", label %"if.1", label %"else.1"
else:
  br label %"merge"
merge:
  %".15" = load i32, i32* %"result"
  %".16" = bitcast [5 x i8]* @"fstr1" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 %".15")
  ret void
if.1:
  store i32 10, i32* %"result"
  br label %"merge.1"
else.1:
  br label %"merge.1"
merge.1:
  br label %"merge"
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr1" = internal constant [5 x i8] c"%i \0a\00"