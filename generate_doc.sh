#!/bin/bash
for dir in ./app/*; do
    if [ -d "$dir" ]; then    
        for f in $dir/*.diag; do            
            if [ -f "$f" ]; then
                echo "Creating .doc/images/${dir##*/}.png"
                seqdiag "$f" -o "doc/images/${dir##*/}.png"
            fi
        done
    fi
done

for f in ./doc/PT-BR/*.md; do
    if [ -f "$f" ]; then
        echo "Creating ${f%.*}-toc.md"
        extracttoc "$f" -i
    fi
done