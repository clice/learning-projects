#!/usr/bin/env bash
set -e

SOURCE_DIR="${1:-.}"
DEST_DIR="backups"

mkdir -p "$DEST_DIR"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
ARCHIVE="$DEST_DIR/backup_$TIMESTAMP.tar.gz"

tar -czf "$ARCHIVE" "$SOURCE_DIR"

echo "Backup criado em: $ARCHIVE"
