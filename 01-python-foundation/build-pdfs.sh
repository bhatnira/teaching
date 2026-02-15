#!/bin/bash
# =============================================================================
# build-pdfs.sh - Compile all LaTeX files and auto-cleanup
# =============================================================================
# Usage: ./build-pdfs.sh [filename.tex]
#   - No arguments: compile all .tex files
#   - With argument: compile specific file

set -e

# Add TeX to PATH
export PATH="/Library/TeX/texbin:$PATH"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Cleanup function
cleanup() {
    echo -e "${YELLOW}Cleaning auxiliary files...${NC}"
    rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.synctex.gz *.fdb_latexmk *.fls 2>/dev/null || true
    echo -e "${GREEN}Cleanup complete!${NC}"
}

# Compile function
compile_tex() {
    local texfile="$1"
    local basename="${texfile%.tex}"
    
    echo -e "${YELLOW}Compiling ${texfile}...${NC}"
    
    # Run pdflatex twice for proper TOC/references
    if pdflatex -interaction=nonstopmode "$texfile" > /dev/null 2>&1; then
        pdflatex -interaction=nonstopmode "$texfile" > /dev/null 2>&1
        echo -e "${GREEN}✓ ${basename}.pdf created${NC}"
        return 0
    else
        echo -e "${RED}✗ Failed to compile ${texfile}${NC}"
        echo "  Run: pdflatex ${texfile} for details"
        return 1
    fi
}

# Main
cd "$(dirname "$0")"

echo "========================================"
echo "LaTeX PDF Builder with Auto-Cleanup"
echo "========================================"

if [ -n "$1" ]; then
    # Compile specific file
    if [ -f "$1" ]; then
        compile_tex "$1"
    else
        echo -e "${RED}File not found: $1${NC}"
        exit 1
    fi
else
    # Compile all .tex files
    for texfile in *.tex; do
        [ -f "$texfile" ] || continue
        compile_tex "$texfile" || true
    done
fi

# Always cleanup
cleanup

echo ""
echo "========================================"
echo "Generated PDFs:"
ls -la *.pdf 2>/dev/null || echo "No PDFs found"
echo "========================================"
