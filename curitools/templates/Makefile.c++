#
# Makefile for the programs
#

CPPFLAGS = -g -Wall -Werror -O2 -lm -std=c++11

CXX=g++

TARGET = prog

obj = $(wildcard *.cpp)

all:  $(TARGET)

$(TARGET): $(obj)
	@echo $< 
	$(CXX) $(CPPFLAGS) $< -o $(TARGET) 
