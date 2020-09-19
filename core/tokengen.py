#!/usr/bin/env python3
import secrets

def generate(length):
    return secrets.token_hex(length)
